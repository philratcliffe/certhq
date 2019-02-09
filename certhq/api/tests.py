from django.test import TestCase
import json
from rest_framework import status

from certhq.certificates.models import Certificate
from certhq.api.serializers import CertificateGetSerializer


class ApiPostTests(TestCase):
    def test_create_record(self):
        response = self.client.post('/api/v1/certificates',
                                    {'pem_data': TEST_EXPIRED_RSA_2048_CERT})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        count = Certificate.objects.all().count()
        expected_object_count = 1
        self.assertEqual(count, expected_object_count)

    def test_create_record_with_correct_subject(self):
        response = self.client.post('/api/v1/certificates',
                                    {'pem_data': TEST_EXPIRED_RSA_2048_CERT})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        cert = Certificate.objects.all()[0]
        expected_subject = "CN=www.example.com, O=Frank4DD, ST=Tokyo, C=JP"
        self.assertEqual(expected_subject, cert.subject)


class ApiGetTests(TestCase):
    def setUp(self):
        Certificate.objects.create(pem_data=TEST_EXPIRED_RSA_2048_CERT)

    def test_list_certificates_returns_one_result(self):
        response = self.client.get('/api/v1/certificates')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json_str = response.content.decode('utf-8')
        res_list = json.loads(json_str)
        expected_number_of_results = 1
        self.assertEqual(len(res_list), expected_number_of_results)


TEST_EXPIRED_RSA_2048_CERT = """
-----BEGIN CERTIFICATE-----
MIIC2jCCAkMCAg38MA0GCSqGSIb3DQEBBQUAMIGbMQswCQYDVQQGEwJKUDEOMAwG
A1UECBMFVG9reW8xEDAOBgNVBAcTB0NodW8ta3UxETAPBgNVBAoTCEZyYW5rNERE
MRgwFgYDVQQLEw9XZWJDZXJ0IFN1cHBvcnQxGDAWBgNVBAMTD0ZyYW5rNEREIFdl
YiBDQTEjMCEGCSqGSIb3DQEJARYUc3VwcG9ydEBmcmFuazRkZC5jb20wHhcNMTIw
ODIyMDUyNzQxWhcNMTcwODIxMDUyNzQxWjBKMQswCQYDVQQGEwJKUDEOMAwGA1UE
CAwFVG9reW8xETAPBgNVBAoMCEZyYW5rNEREMRgwFgYDVQQDDA93d3cuZXhhbXBs
ZS5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC0z9FeMynsC8+u
dvX+LciZxnh5uRj4C9S6tNeeAlIGCfQYk0zUcNFCoCkTknNQd/YEiawDLNbxBqut
bMDZ1aarys1a0lYmUeVLCIqvzBkPJTSQsCopQQ9V8WuT252zzNzs68dVGNdCJd5J
NRQykpwexmnjPPv0mvj7i8XgG379TyW6P+WWV5okeUkXJ9eJS2ouDYdR2SM9BoVW
+FgxDu6BmXhozW5EfsnajFp7HL8kQClI0QOc79yuKl3492rH6bzFsFn2lfwWy9ic
7cP8EpCTeFp1tFaD+vxBhPZkeTQ1HKx6hQ5zeHIB5ySJJZ7af2W8r4eTGYzbdRW2
4DDHCPhZAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAQMv+BFvGdMVzkQaQ3/+2noVz
/uAKbzpEL8xTcxYyP3lkOeh4FoxiSWqy5pGFALdPONoDuYFpLhjJSZaEwuvjI/Tr
rGhLV1pRG9frwDFshqD2Vaj4ENBCBh6UpeBop5+285zQ4SI7q4U9oSebUDJiuOx6
+tZ9KynmrbJpTSi0+BM=
-----END CERTIFICATE-----
"""
