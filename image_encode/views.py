from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
from rest_framework import viewsets, generics, mixins
from .serializers import ImageSerializer,ImageDecodeSerializer
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from rest_framework.response import Response
import os
import pybase64


class ImageEncodeViewSet(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):

        data = request.FILES['image'] # or self.files['image'] in your form
        file_name = f"tmp.{data.name.split('.')[-1]}"
        path = default_storage.save(file_name, ContentFile(data.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        
        with open(tmp_file, 'rb') as f:
            image_data = f.read()
        
        base64_image = pybase64.b64encode(image_data).decode('utf-8')

        return Response(data= {'encoded_image':base64_image}, status=200)


class ImageDecodeViewSet(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = ImageDecodeSerializer

    def post(self, request, *args, **kwargs):

        
        image_data = pybase64.b64decode(base64_image_data)

        return Response(data= {'encoded_image':base64_image}, status=200)