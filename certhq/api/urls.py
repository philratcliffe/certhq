from django.urls import path
from .views import CertificateListCreate, CertificateRetrieveDestroy

app_name = 'api'

urlpatterns = [
    path('certificates', CertificateListCreate.as_view(), name='certificates'),
    path(
        'certificates/<int:pk>/',
        CertificateRetrieveDestroy.as_view(),
        name='certificate_retrieve_destroy')
]
