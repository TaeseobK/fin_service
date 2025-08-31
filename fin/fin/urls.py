"""
URL configuration for fin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import DEBUG
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from fin_master.views import CoaViewSet, ProductViewSet, ProductPrincipalViewSet, ProductCodeViewSet, UnitProductViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static
from fin_dump.views import metrics_view
from drf_spectacular_extras.views import SpectacularScalarView

router = DefaultRouter()

router.register(r'master/coa', CoaViewSet)
router.register(r'master/product', ProductViewSet)
router.register(r'master/product-principal', ProductPrincipalViewSet)
router.register(r'master/product-code', ProductCodeViewSet)
router.register(r'master/unit-product', UnitProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/fin/', include(router.urls)),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/scalar/', SpectacularScalarView.as_view(url_name='schema'), name='scalar-ui'),

    path('metrics/', metrics_view, name='metrics'),
]

if DEBUG:
    urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)