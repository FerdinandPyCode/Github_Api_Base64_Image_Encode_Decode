from django.urls import path, include
from .views import UserInfos

urlpatterns = [
    path('', UserInfos.as_view(), name = 'github_user_infos'),
]