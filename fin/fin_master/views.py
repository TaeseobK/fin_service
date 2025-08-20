from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import *
from .serializers import *
from .filters import *
from fin.config import *
from fin.thread_locals import *

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
    
# ==============================
# BudgetCode
# ==============================
@extend_schema(tags=["BudgetCode"])
class BudgetCodeViewSet(BaseViewSet):
    queryset = BudgetCode.objects.all().order_by('-created_by')
    serializer_class = BudgetCodeSerializer
    filterset_class = BudgetCodeFilter

    @extend_schema(
        description=f"{inspect.getdoc(BaseViewSet)}\n\nAmbil daftar company dengan pagination & filter.",
        parameters=[
            *generate_filter_parameters_from_basefilter(BudgetCode, BaseFilter),
            *BASE_PARAMS
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
        description=f"{inspect.getdoc(BaseViewSet)}\n\nAmbil daftar company dengan pagination & filter.",
        parameters=[
            *generate_filter_parameters_from_basefilter(YearlyTarget, BaseFilter),
            *BASE_PARAMS
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
        description=f"{inspect.getdoc(BaseViewSet)}\n\nAmbil daftar company dengan pagination & filter.",
        parameters=[
            *generate_filter_parameters_from_basefilter(MonthlyTarget, BaseFilter),
            *BASE_PARAMS
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
        description=f"{inspect.getdoc(BaseViewSet)}\n\nAmbil daftar company dengan pagination & filter.",
        parameters=[
            *generate_filter_parameters_from_basefilter(UnitTarget, BaseFilter),
            *BASE_PARAMS
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
        description=f"{inspect.getdoc(BaseViewSet)}\n\nAmbil daftar company dengan pagination & filter.",
        parameters=[
            *generate_filter_parameters_from_basefilter(TargetProduct, BaseFilter),
            *BASE_PARAMS
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
        description=f"{inspect.getdoc(BaseViewSet)}\n\nAmbil daftar company dengan pagination & filter.",
        parameters=[
            *generate_filter_parameters_from_basefilter(BudgetUnitYear, BaseFilter),
            *BASE_PARAMS
        ],
        responses={200: BudgetUnitYearSerializer}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)