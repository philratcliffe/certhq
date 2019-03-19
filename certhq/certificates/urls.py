from django.urls import path
from .views import CertificateList, CertificateDetail

urlpatterns = [
    path('', CertificateList.as_view(), name='certificates'),
    path('<int:pk>', CertificateDetail.as_view(), name='certificate_detail'),
]
