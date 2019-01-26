from django.urls import include
from django.urls import path

from . import views

app_name='users'

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
]
