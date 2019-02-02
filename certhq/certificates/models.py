from django.db import models

from OpenSSL import crypto

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from model_utils.models import TimeStampedModel


def stringify_x509_name(x509_name):
    """Returns a string representation of an X509Name object"""
    return ', '.join(
        '{0}={1}'.format(key.decode('utf-8'), val.decode('utf-8'))
        for key, val in x509_name.get_components()[::-1])



class CertificateManager(models.Manager):
    def create_certificate(self, pem_data):
        c = crypto.load_certificate(crypto.FILETYPE_PEM, pem_data)
        subject = stringify_x509_name(c.get_subject())
        issuer = stringify_x509_name(c.get_issuer())
        cn = c.get_subject().CN
        cert = Certificate(
            pem_data=pem_data, subject=subject, issuer=issuer, cn=cn)
        cert.save()
        return cert


class Certificate(TimeStampedModel):
    pem_data = models.TextField()
    issuer = models.CharField(max_length=2048)
    subject = models.CharField(max_length=2048, blank=True)
    cn = models.CharField(max_length=2048, blank=True)
    sha256_fingerprint = models.CharField(max_length=64, unique=True)

    objects = CertificateManager()

    def __str__(self):
        return self.cn
