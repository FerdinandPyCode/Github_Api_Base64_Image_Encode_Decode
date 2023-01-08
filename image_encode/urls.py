from django.urls import path, include
from .views import ImageEncodeViewSet,ImageDecodeViewSet


urlpatterns = [
    path('encode', ImageEncodeViewSet.as_view(), name = 'encode_image'),
    path('decode',ImageDecodeViewSet.as_view(), name= 'decode_image')
]