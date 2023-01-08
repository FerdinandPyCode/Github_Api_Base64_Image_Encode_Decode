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
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):

        data = request.FILES

        image_file = data['upload_a_txt_file_with_base64_string_of_the_image']
        path = default_storage.save('fichier.txt', ContentFile(image_file.read()))
        txt_file_path = os.path.join(settings.MEDIA_ROOT, path)
        string = ''
        with open(txt_file_path, 'r') as f:
            string = f.read()
        
        image_data = pybase64.b64decode(string)

        path = default_storage.save('image.jpg', ContentFile(image_data))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)

        with open(tmp_file, 'wb') as f:
            f.write(image_data)
        
        return Response(data= {'decoded_image': tmp_file}, status=200)