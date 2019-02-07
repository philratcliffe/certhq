from certhq.certificates.models import Certificate
from rest_framework import serializers


class CertificatePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certificate
        fields = ('pem_data',)



class CertificateGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certificate
        fields = ('pem_data', 'subject', 'issuer', 'cn', 'sha256_fingerprint')




