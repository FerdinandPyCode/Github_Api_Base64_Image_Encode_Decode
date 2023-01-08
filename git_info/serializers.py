from rest_framework import serializers


class UserGithubIdSerializers(serializers.Serializer):
    user_id = serializers.CharField(max_length=102)

class GithubUserInfos(serializers.Serializer):
    pass