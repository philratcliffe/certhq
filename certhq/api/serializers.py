from certhq.certificates.models import Certificate
from rest_framework import serializers


class CertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certificate
        fields = ('pem_data',)


