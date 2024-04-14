from django.urls import path
from .views import sign_up


urlpatterns = [
    path('register/', sign_up, name='sign_up')
]