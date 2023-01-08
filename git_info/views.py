from django.shortcuts import render
# importing the requests library
from rest_framework.response import Response
import requests
from .serializers import UserGithubIdSerializers
from rest_framework import viewsets, generics, mixins


class UserInfos(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = UserGithubIdSerializers

    def post(self, request, *args , **kargs):
        data = request.data

        user_id = data['user_id']

        # api-endpoint
        URL = f"https://api.github.com/users/{user_id}"
        
        # defining a params dict for the parameters to be sent to the API
        # PARAMS = {'address':location}
        
        # sending get request and saving the response as response object
        r = requests.get(url = URL)
        
        # extracting data in json format
        infos = r.json()

        return Response(data = infos, status = 200)

