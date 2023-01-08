from rest_framework import serializers

class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField()

class ImageDecodeSerializer(serializers.Serializer):
    upload_a_txt_file_with_base64_string_of_the_image = serializers.FileField()