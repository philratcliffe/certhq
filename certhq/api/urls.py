from django.urls import path
from .views import CertificateList

urlpatterns = [
    path('certificates', CertificateList.as_view())
]
