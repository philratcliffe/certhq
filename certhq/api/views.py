from certhq.certificates.models import Certificate
from rest_framework import generics
from .serializers import CertificatePostSerializer, CertificateGetSerializer


class CertificateListCreate(generics.ListCreateAPIView):
    """
    API endpoint for listing certificates or adding a cert to the database.
    """
    queryset = Certificate.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CertificatePostSerializer
        return CertificateGetSerializer


class CertificateRetrieve(generics.RetrieveAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateGetSerializer
