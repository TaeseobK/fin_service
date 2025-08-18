from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import *
from .serializers import *
from .filters import *
from fin.config import *
from fin.thread_locals import *

SOFTDELETE_PARAMS = [
    OpenApiParameter("include_deleted", bool, OpenApiParameter.QUERY,
                     description="Jika true, tampilkan semua data termasuk yang sudah soft delete."),
    OpenApiParameter("only_deleted", bool, OpenApiParameter.QUERY,
                     description="Jika true, tampilkan hanya data yang sudah soft delete."),
]

# ==============================
# Coa
# ==============================
@extend_schema(tags=['Coa'])
class CoaViewSet(BaseViewSet):
    queryset = Coa.objects.all()
    serializer_class = CoaSerializer
    filterset_class = CoaFilter

    @extend_schema(
        summary="List Coa",
        description="Ambil daftar coa dengan pagination & filter.",
        parameters=[
            OpenApiParameter("page", int, OpenApiParameter.QUERY, description="Halaman"),
            OpenApiParameter("page_size", int, OpenApiParameter.QUERY, description="Jumlah item per halaman"),
            OpenApiParameter("is_active", bool, OpenApiParameter.QUERY, description="True=aktif, False=soft deleted"),
            OpenApiParameter("code", str, OpenApiParameter.QUERY, description="Kode perusahaan"),
            OpenApiParameter("name", str, OpenApiParameter.QUERY, description="Nama perusahaan (partial match)"),
            OpenApiParameter("parent_id", int, OpenApiParameter.QUERY, description="Filter berdasarkan parent ID"),
            *SOFTDELETE_PARAMS
        ],
        responses={200: CoaSerializer}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
# ==============================
# Budget Classification
# ==============================
@extend_schema(tags=['Budget Class'])
class BudgetClassViewSet(BaseViewSet):
    queryset = BudgetClass.objects.all()
    serializer_class = BudgetClassSerializer
    filterset_class = BudgetClassFilter

    @extend_schema(
        summary="List Code Budget",
        description="Ambil daftar code budget dengan pagination & filter.",
        parameters=[
            OpenApiParameter("page", int, OpenApiParameter.QUERY, description="Halaman"),
            OpenApiParameter("page_size", int, OpenApiParameter.QUERY, description="Jumlah item per halaman"),
            OpenApiParameter("is_active", bool, OpenApiParameter.QUERY, description="True=aktif, False=soft deleted"),
            OpenApiParameter("code", str, OpenApiParameter.QUERY, description="Kode perusahaan"),
            OpenApiParameter("name", str, OpenApiParameter.QUERY, description="Nama perusahaan (partial match)"),
            OpenApiParameter("parent_id", int, OpenApiParameter.QUERY, description="Filter berdasarkan parent ID"),
            *SOFTDELETE_PARAMS
        ],
        responses={200: BudgetClassSerializer}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

# ==============================
# Annual Budget
# ==============================
@extend_schema(tags=['Annual Budgets'])
class AnnualBudgetViewSet(BaseViewSet):
    queryset = AnnualBudget.objects.all()
    serializer_class = AnnualBudgetSerializer
    filterset_class = AnnualBudgetFilter

    @extend_schema(
        summary="List Annual Budget",
        description="Ambil daftar coa dengan pagination & filter.",
        parameters=[
            OpenApiParameter("page", int, OpenApiParameter.QUERY, description="Halaman"),
            OpenApiParameter("page_size", int, OpenApiParameter.QUERY, description="Jumlah item per halaman"),
            OpenApiParameter("is_active", bool, OpenApiParameter.QUERY, description="True=aktif, False=soft deleted"),
            OpenApiParameter("code", str, OpenApiParameter.QUERY, description="Kode perusahaan"),
            OpenApiParameter("name", str, OpenApiParameter.QUERY, description="Nama perusahaan (partial match)"),
            OpenApiParameter("parent_id", int, OpenApiParameter.QUERY, description="Filter berdasarkan parent ID"),
            *SOFTDELETE_PARAMS
        ],
        responses={200: AnnualBudgetSerializer}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

# ==============================
# Monthly Budget Classification
# ==============================
@extend_schema(tags=['Monhtly Budgets'])
class MonhtlyBudgetViewSet(BaseViewSet):
    queryset = MonthlyBudget.objects.all()
    serializer_class = MonthlyBudgetSerializer
    filterset_class = MonthlyBudgetFilter

    @extend_schema(
        summary="List Monthly Budget",
        description="Ambil daftar budget monthly dengan pagination & filter.",
        parameters=[
            OpenApiParameter("page", int, OpenApiParameter.QUERY, description="Halaman"),
            OpenApiParameter("page_size", int, OpenApiParameter.QUERY, description="Jumlah item per halaman"),
            OpenApiParameter("is_active", bool, OpenApiParameter.QUERY, description="True=aktif, False=soft deleted"),
            OpenApiParameter("code", str, OpenApiParameter.QUERY, description="Kode perusahaan"),
            OpenApiParameter("name", str, OpenApiParameter.QUERY, description="Nama perusahaan (partial match)"),
            OpenApiParameter("parent_id", int, OpenApiParameter.QUERY, description="Filter berdasarkan parent ID"),
            *SOFTDELETE_PARAMS
        ],
        responses={200: MonthlyBudgetSerializer}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)