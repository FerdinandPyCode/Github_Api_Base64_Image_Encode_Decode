from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
from rest_framework import viewsets, generics, mixins
from .serializers import ImageSerializer
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
        
        base64_image = pybase64.b64encode(tmp_file).decode('utf-8')

        return Response(data= {'encoded_image':base64_image}, status=200)