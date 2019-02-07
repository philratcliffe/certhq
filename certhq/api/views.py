from certhq.certificates.models import Certificate
from rest_framework import generics
from .serializers import CertificatePostSerializer, CertificateGetSerializer


class CertificateList(generics.ListCreateAPIView):
    """
    API endpoint that allows certificates to be viewed or created.
    """
    queryset = Certificate.objects.all()


    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CertificatePostSerializer
        return CertificateGetSerializer

