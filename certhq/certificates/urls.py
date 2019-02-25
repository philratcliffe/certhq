from django.urls import path
from .views import CertificateList

urlpatterns = [
    path('', CertificateList.as_view(), name='certificates'),
]
