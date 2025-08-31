from drf_spectacular.utils import extend_schema, OpenApiParameter

import requests
from .models import *
from .serializers import *
from .filters import *
from fin.config import *
from fin.thread_locals import *
from fin.local_settings import *

import inspect


BASE_PARAMS = [
    OpenApiParameter("include_deleted", OpenApiTypes.BOOL, OpenApiParameter.QUERY,
                     description="If true, get all data with deleted data."),
    OpenApiParameter("only_deleted", OpenApiTypes.BOOL, OpenApiParameter.QUERY,
                     description="If true, get all data only deleted data."),
    OpenApiParameter("page", OpenApiTypes.INT, OpenApiParameter.QUERY,
                     description="Return which page you want to return."),
    OpenApiParameter("page_size", OpenApiTypes.INT, OpenApiParameter.QUERY,
                     description="Return the count of data each page."),
    OpenApiParameter("page_size", OpenApiTypes.STR, OpenApiParameter.QUERY,
                     description="Return the count of data each page."),
    OpenApiParameter("search", OpenApiTypes.STR, OpenApiParameter.QUERY,
                     description="Search based on name (WHERE LIKE %<value>%) and Code (WHERE = <value>)"),
    OpenApiParameter("fields", OpenApiTypes.STR, OpenApiParameter.QUERY,
                     description="Only get the fields you want\n\nexample:\n\n?fields=name,code,created_at"),
    OpenApiParameter("exclude", OpenApiTypes.STR, OpenApiParameter.QUERY,
                     description="Remove the fields you want\n\nexample:\n\n?exclude=created_at,created_by,updated_at,updated_by"),
]

# ==============================
# Coa
# ==============================
@extend_schema(tags=["Coa"])
class CoaViewSet(BaseViewSet):
    queryset = Coa.objects.all().order_by('-created_by')
    serializer_class = CoaSerializer
    filterset_class = CoaFilter

    @extend_schema(
        description=f"{inspect.getdoc(BaseViewSet)}\n\nAmbil daftar company dengan pagination & filter.",
        parameters=[
            *generate_filter_parameters_from_basefilter(Coa, BaseFilter),
            *BASE_PARAMS
        ],
        responses={200: CoaSerializer}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
@extend_schema(tags=["Product"])
class ProductViewSet(BaseViewSet):
    queryset = Product.objects.all().prefetch_related("product_codes", "product_principals", "product_units", "target_estimations")
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    
    @extend_schema(
        description=f"{inspect.getdoc(BaseViewSet)}\n\nAmbil daftar company dengan pagination & filter.",
        parameters=[
            *generate_filter_parameters_from_basefilter(Product, BaseFilter),
            *BASE_PARAMS
        ], 
        responses={200: ProductSerializer}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
@extend_schema(tags=["ProductCode"])
class ProductCodeViewSet(BaseViewSet):
    queryset = ProductCode.objects.all().order_by('-created_by')
    serializer_class = ProductCodeSerializer
    filterset_class = ProductCodeFilter

    @extend_schema(
        description=f"{inspect.getdoc(BaseViewSet)}\n\nAmbil daftar company dengan pagination & filter.",
        parameters=[
            *generate_filter_parameters_from_basefilter(ProductCode, BaseFilter),
            *BASE_PARAMS
        ],
        responses={200: ProductCodeSerializer}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

@extend_schema(tags=["ProductPrincipal"])
class ProductPrincipalViewSet(BaseViewSet):
    queryset = ProductPrincipal.objects.all().order_by('-created_by')
    serializer_class = ProductPrincipalSerializer
    filterset_class = ProductPrincipalFilter

    @extend_schema(
        description=f"{inspect.getdoc(BaseViewSet)}\n\nAmbil daftar company dengan pagination & filter.",
        parameters=[
            *generate_filter_parameters_from_basefilter(ProductPrincipal, BaseFilter),
            *BASE_PARAMS
        ],
        responses={200: ProductPrincipalSerializer}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

@extend_schema(tags=["UnitProduct"])
class UnitProductViewSet(BaseViewSet):
    queryset = UnitProduct.objects.all().order_by('-created_by')
    serializer_class = UnitProductSerializer
    filterset_class = UnitProductFilter

    @extend_schema(
        description=f"{inspect.getdoc(BaseViewSet)}\n\nAmbil daftar company dengan pagination & filter.",
        parameters=[
            *generate_filter_parameters_from_basefilter(UnitProduct, BaseFilter),
            *BASE_PARAMS
        ],
        responses={200: UnitProductSerializer}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)