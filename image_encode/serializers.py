from rest_framework import serializers

class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField()

class ImageDecodeSerializer(serializers.Serializer):
    image_string = serializers.CharField(max_length=20000)