from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from usuario.views import UserViewSet
from core.views import *


from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('artefact-images', ArtefactImageViewSet)
router.register('collections', CollectionViewSet)
router.register('localizations', LocalizationViewSet)
router.register('raw-materials', RawMaterialViewSet)
router.register('sub-types', SubTypeViewSet)
router.register('artefacts', ArtefactViewSet, basename="artefacts")
router.register('archaelogical-sites', ArchaeologicalSiteViewSet)
router.register('log-movements', LogMovementViewSet)
router.register('reserves', ReserveViewSet)
router.register('log-changes', LogChangesViewSet)
router.register('conservation-actions', ConservationActionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls))
]
