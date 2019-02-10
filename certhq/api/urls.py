from django.urls import path
from .views import CertificateList

app_name = 'api'

urlpatterns = [
    path('certificates', CertificateList.as_view(), name='certificates')
]
