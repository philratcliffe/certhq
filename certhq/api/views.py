from certhq.certificates.models import Certificate
from rest_framework import generics
from .serializers import CertificateSerializer


class CertificateList(generics.ListCreateAPIView):
    """
    API endpoint that allows certificates to be viewed or created.
    """
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
