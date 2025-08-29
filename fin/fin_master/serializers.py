from rest_framework import serializers
from .models import *
from fin.local_settings import *
import requests
from drf_spectacular.utils import extend_schema_field

"""

⚠ Heed This Warning, Successor ⚠

Beneath these lines lies an ancient incantation, woven into the very veins of every serializer that breathes life into this realm. 
Its essence flows unseen through the arteries of our code, binding chaos and order in a fragile truce. 
To alter it without true understanding — and without the blessing of the Elders — is to tear open the gates of ruin. 
Data will twist, APIs will scream, and the system will collapse into a silence more dreadful than death.

Remember, this is no mere function, but a seal of power that holds the balance. 
Break it, and no redemption shall follow. 
If you read this, successor, know this truth: let it remain untouched… or prepare to have your name whispered as a cautionary tale in the dim, 
haunted corners of every developer's gathering.

May God of Knowledge Bless You.



"""

class UserField(serializers.Field):
    """
    Custom field buat ganti integer user_id jadi dict user data.
    Ambil dari context['users_map'].
    """
    def to_representation(self, value):
        users_map = self.context.get("users_map", {})
        data = users_map.get(value, {"id": value}) if value else None
        return data
    
UserField = extend_schema_field(
    {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "username": {"type": "string"},
            "email": {"type": "string"}
        }
    }
)(UserField)

class DynamicModelSerializer(serializers.ModelSerializer):
    """
    Bisa filter 'fields' dan 'exclude' (diambil dari kwargs atau query_params).
    """
    def __init__(self, *args, **kwargs):
        # Ambil context request
        context = kwargs.get('context', {})
        request = context.get('request')

        # Ambil fields & exclude dari kwargs
        fields = kwargs.pop('fields', None)
        exclude = kwargs.pop('exclude', None)

        # Kalau ada query_params, ambil dari sana
        if request:
            qp = request.query_params
            if fields is None and 'fields' in qp:
                fields = [f.strip() for f in qp.get('fields', '').split(',') if f.strip()]
            if exclude is None and 'exclude' in qp:
                exclude = [f.strip() for f in qp.get('exclude', '').split(',') if f.strip()]

        super().__init__(*args, **kwargs)

        # Filter fields
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

        # Exclude fields
        if exclude is not None:
            for field_name in exclude:
                self.fields.pop(field_name, None)
    
    def get_fields(self):
        fields = super().get_fields()

        # ganti semua *_by jadi UserField
        for by_field in ["created_by", "updated_by", "deleted_by"]:
            if by_field in fields:
                fields[by_field] = UserField()

        return fields

class BaseTreeSerializer(DynamicModelSerializer):
    """
    Dasar serializer pohon:
    - Menyembunyikan 'children' saat render mode parent chain.
    - Menyembunyikan 'parent' saat render mode children tree.
    - Mencegah recursion karena field lawan di-drop SEBELUM to_representation jalan.
    """
    TREE_PARENT_FIELD = 'parent'     # override kalau nama field parent beda
    TREE_CHILDREN_FIELD = 'children' # override kalau related_name beda

    def __init__(self, *args, **kwargs):
        # mode opsional via arg; default ambil dari context
        self.tree_mode = kwargs.pop('tree_mode', None)
        super().__init__(*args, **kwargs)

    def get_fields(self):
        fields = super().get_fields()
        mode = self.tree_mode or self.context.get('_mode')

        if mode == 'parent':
            # Saat berjalan ke atas, jangan ikutkan children
            fields.pop(self.TREE_CHILDREN_FIELD, None)
        elif mode == 'children':
            # Saat berjalan ke bawah, jangan ikutkan parent
            fields.pop(self.TREE_PARENT_FIELD, None)

        return fields


class SmartRecursive(serializers.Serializer):
    """
    Helper rekursif universal:
    - Bisa dipakai di semua serializer turunan BaseTreeSerializer.
    - Tidak wajib passing serializer_class, otomatis ambil dari induknya.
    - Depth guard mencegah infinite recursion.
    """
    def __init__(self, *args, **kwargs):
        self.mode = kwargs.pop('mode', None)  # "parent" | "children"
        super().__init__(*args, **kwargs)

    def get_serializer_class(self):
        """
        Cari serializer class induk dengan aman.
        Hindari infinite recursion (jangan ambil SmartRecursive lagi).
        """
        parent = getattr(self, 'parent', None)
        if parent is None:
            return None

        # Ambil serializer induk langsung
        if isinstance(parent, serializers.ListSerializer):
            parent = parent.parent

        if parent and not isinstance(parent, SmartRecursive):
            return parent.__class__

        return None

    def to_representation(self, value):
        serializer_class = self.get_serializer_class()
        if serializer_class is None:
            return {
                'id': getattr(value, 'id', None),
                'name': getattr(value, 'name', None)
            }

        context = dict(self.context or {})
        context['_mode'] = self.mode

        # Ambil max_depth dari query_params jika ada
        if 'request' in context:
            try:
                query_depth = int(context['request'].query_params.get('max_depth', 10))
            except ValueError:
                query_depth = 10
            context['_max_depth'] = query_depth
        else:
            context['_max_depth'] = context.get('_max_depth', 10)

        # Depth guard
        depth = int(context.get('_depth', 0))
        max_depth = int(context['_max_depth'])
        if depth >= max_depth:
            return {
                'id': getattr(value, 'id', None),
                'name': getattr(value, 'name', None)
            }
        context['_depth'] = depth + 1

        kwargs = {'context': context}
        if 'fields' in context and hasattr(serializer_class, 'get_fields'):
            kwargs['fields'] = context['fields']

        return serializer_class(value, **kwargs).data

class ProductCodeSerializer(BaseTreeSerializer):

    class Meta:
        model = ProductCode
        fields = '__all__'
        
class ProductPrincipalSerializer(BaseTreeSerializer):
    
    class Meta:
        model = ProductPrincipal
        fields = '__all__'
        
class UnitProductSerializer(BaseTreeSerializer):

    class Meta:
        model = UnitProduct
        fields = '__all__'

class ProductSerializer(BaseTreeSerializer):
    product_codes = ProductCodeSerializer(many=True)
    product_principals = ProductPrincipalSerializer(many=True)
    product_units = UnitProductSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
        
class CoaSerializer(BaseTreeSerializer):
    
    class Meta:
        model = Coa
        fields = '__all__'

class UnitBudgetSerializer(BaseTreeSerializer):
    
    class Meta:
        model = UnitBudget
        fields = '__all__'

class BudgetSerializer(BaseTreeSerializer):
    unit = UnitBudgetSerializer(many=True)
    coa = CoaSerializer(many=True)
    
    class Meta:
        model = Budget
        fields = '__all__'
        
class TargetEstimationSerializer(BaseTreeSerializer):
    product = ProductSerializer()

    class Meta:
        model = TargetEstimation
        fields = '__all__'