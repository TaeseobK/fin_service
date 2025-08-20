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
    queryset = Coa.objects.all().order_by('-created_by')
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
# BudgetCode
# ==============================
@extend_schema(tags=['BudgetCode'])
class BudgetCodeViewSet(BaseViewSet):
    queryset = BudgetCode.objects.all().order_by('-created_by')
    serializer_class = BudgetCodeSerializer
    filterset_class = BudgetCodeFilter

    @extend_schema(
        summary="List Budget Codes",
        description="Ambil daftar budget code dengan pagination & filter.",
        parameters=[
            OpenApiParameter("page", int, OpenApiParameter.QUERY, description="Halaman"),
            OpenApiParameter("page_size", int, OpenApiParameter.QUERY, description="Jumlah item per halaman"),
            OpenApiParameter("code", str, OpenApiParameter.QUERY, description="Kode budget"),
            OpenApiParameter("name", str, OpenApiParameter.QUERY, description="Nama budget"),
            *SOFTDELETE_PARAMS
        ],
        responses={200: BudgetCodeSerializer}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


# ==============================
# YearlyTarget
# ==============================
@extend_schema(tags=['YearlyTarget'])
class YearlyTargetViewSet(BaseViewSet):
    queryset = YearlyTarget.objects.all()
    serializer_class = YearlyTargetSerializer
    filterset_class = YearlyTargetFilter

    @extend_schema(
        summary="List Yearly Targets",
        description="Ambil daftar yearly target dengan pagination & filter.",
        parameters=[
            OpenApiParameter("page", int, OpenApiParameter.QUERY, description="Halaman"),
            OpenApiParameter("page_size", int, OpenApiParameter.QUERY, description="Jumlah item per halaman"),
            OpenApiParameter("year", int, OpenApiParameter.QUERY, description="Tahun target"),
            OpenApiParameter("company_id", int, OpenApiParameter.QUERY, description="ID Perusahaan"),
            *SOFTDELETE_PARAMS
        ],
        responses={200: YearlyTargetSerializer}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


# ==============================
# MonthlyTarget
# ==============================
@extend_schema(tags=['MonthlyTarget'])
class MonthlyTargetViewSet(BaseViewSet):
    queryset = MonthlyTarget.objects.all()
    serializer_class = MonthlyTargetSerializer
    filterset_class = MonthlyTargetFilter

    @extend_schema(
        summary="List Monthly Targets",
        description="Ambil daftar monthly target dengan pagination & filter.",
        parameters=[
            OpenApiParameter("page", int, OpenApiParameter.QUERY, description="Halaman"),
            OpenApiParameter("page_size", int, OpenApiParameter.QUERY, description="Jumlah item per halaman"),
            OpenApiParameter("month", int, OpenApiParameter.QUERY, description="Bulan (1-12)"),
            *SOFTDELETE_PARAMS
        ],
        responses={200: MonthlyTargetSerializer}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


# ==============================
# UnitTarget
# ==============================
@extend_schema(tags=['UnitTarget'])
class UnitTargetViewSet(BaseViewSet):
    queryset = UnitTarget.objects.all()
    serializer_class = UnitTargetSerializer
    filterset_class = UnitTargetFilter

    @extend_schema(
        summary="List Unit Targets",
        description="Ambil daftar target unit dengan pagination & filter.",
        parameters=[
            OpenApiParameter("page", int, OpenApiParameter.QUERY, description="Halaman"),
            OpenApiParameter("page_size", int, OpenApiParameter.QUERY, description="Jumlah item per halaman"),
            OpenApiParameter("unit_id", int, OpenApiParameter.QUERY, description="ID Unit"),
            *SOFTDELETE_PARAMS
        ],
        responses={200: UnitTargetSerializer}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


# ==============================
# TargetProduct
# ==============================
@extend_schema(tags=['TargetProduct'])
class TargetProductViewSet(BaseViewSet):
    queryset = TargetProduct.objects.all()
    serializer_class = TargetProductSerializer
    filterset_class = TargetProductFilter

    @extend_schema(
        summary="List Target Products",
        description="Ambil daftar target produk dengan pagination & filter.",
        parameters=[
            OpenApiParameter("page", int, OpenApiParameter.QUERY, description="Halaman"),
            OpenApiParameter("page_size", int, OpenApiParameter.QUERY, description="Jumlah item per halaman"),
            OpenApiParameter("product_id", int, OpenApiParameter.QUERY, description="ID Produk"),
            OpenApiParameter("year", int, OpenApiParameter.QUERY, description="Tahun"),
            *SOFTDELETE_PARAMS
        ],
        responses={200: TargetProductSerializer}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


# ==============================
# BudgetUnitYear
# ==============================
@extend_schema(tags=['BudgetUnitYear'])
class BudgetUnitYearViewSet(BaseViewSet):
    queryset = BudgetUnitYear.objects.all()
    serializer_class = BudgetUnitYearSerializer
    filterset_class = BudgetUnitYearFilter

    @extend_schema(
        summary="List Budget Unit Year",
        description="Ambil daftar budget unit per tahun dengan pagination & filter.",
        parameters=[
            OpenApiParameter("page", int, OpenApiParameter.QUERY, description="Halaman"),
            OpenApiParameter("page_size", int, OpenApiParameter.QUERY, description="Jumlah item per halaman"),
            OpenApiParameter("unit_id", int, OpenApiParameter.QUERY, description="ID Unit"),
            OpenApiParameter("year", int, OpenApiParameter.QUERY, description="Tahun"),
            *SOFTDELETE_PARAMS
        ],
        responses={200: BudgetUnitYearSerializer}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
