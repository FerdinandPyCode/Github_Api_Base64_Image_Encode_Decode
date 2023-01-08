from django.urls import path, include
from .views import ImageEncodeViewSet


urlpatterns = [
    path('', ImageEncodeViewSet.as_view(), name = 'encode_image'),
]