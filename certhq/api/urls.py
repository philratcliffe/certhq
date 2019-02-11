from django.urls import path
from .views import CertificateListCreate, CertificateRetrieve

app_name = 'api'

urlpatterns = [
    path('certificates', CertificateListCreate.as_view(), name='certificates'),
    path(
        'certificates/<int:pk>/',
        CertificateRetrieve.as_view(),
        name='certificate_detail')
]
