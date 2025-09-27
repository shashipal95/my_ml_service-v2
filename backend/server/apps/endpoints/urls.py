# backend/server/apps/endpoints/urls.py
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from apps.endpoints.views import PredictView

from apps.endpoints.views import (
    EndpointViewSet,
    MLAlgorithmViewSet,
    MLAlgorithmStatusViewSet,
    MLRequestViewSet,
)

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")

urlpatterns = [
    path("api/v1/", include(router.urls)),
    # Added predict URL using re_path
    re_path(
        r"^api/v1/(?P<endpoint_name>.+)/predict$",
        PredictView.as_view(),
        name="predict"
    ),
]
