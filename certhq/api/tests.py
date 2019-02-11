from django.urls import reverse
import json
from rest_framework import status
from rest_framework.test import APITestCase

from certhq.certificates.models import Certificate
from certhq.api.serializers import CertificateGetSerializer


class ApiPostTests(APITestCase):
    def setUp(self):
        self.url = reverse('api:certificates')
        self.test_pem_cert = TEST_EXPIRED_RSA_2048_CERT

    def test_create_record(self):
        response = self.client.post(self.url, {'pem_data': self.test_pem_cert})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Certificate.objects.count(), 1)

    def test_create_record_with_correct_subject(self):
        response = self.client.post(self.url, {'pem_data': self.test_pem_cert})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        cert = Certificate.objects.all()[0]
        expected_subject = "CN=www.example.com, O=Frank4DD, ST=Tokyo, C=JP"
        self.assertEqual(expected_subject, cert.subject)

    def test_create_record_with_correct_pem_data(self):
        response = self.client.post(self.url, {'pem_data': self.test_pem_cert})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        resp = json.loads(response.content)
        self.assertEqual(self.test_pem_cert, resp['pem_data'])


class ApiListTestsWithOneRecord(APITestCase):
    def setUp(self):
        Certificate.objects.create(pem_data=TEST_EXPIRED_RSA_2048_CERT)
        obj_dict = Certificate.objects.all()[0].__dict__

        self.url = reverse('api:certificates')
        self.expected_cn = obj_dict['cn']

    def test_list_certificates_returns_one_result(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        resp = json.loads(response.content)
        obj = Certificate.objects.all()[0]
        self.assertEqual(len(resp), Certificate.objects.count())

    def test_list_certificates_returns_expected_cn(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        resp = json.loads(response.content)
        self.assertEqual(resp[0]['cn'], self.expected_cn)


class ApiGetCertificateTestsWithOneRecord(APITestCase):
    def setUp(self):
        Certificate.objects.create(pem_data=TEST_EXPIRED_RSA_2048_CERT)
        obj_dict = Certificate.objects.all()[0].__dict__

        self.url = reverse('api:certificate_detail', kwargs={'pk': 1})
        self.expected_cn = obj_dict['cn']

    def test_get_certificates_returns_expected_cn(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        resp = json.loads(response.content)
        self.assertEqual(resp['cn'], self.expected_cn)


TEST_EXPIRED_RSA_2048_CERT = """-----BEGIN CERTIFICATE-----
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
-----END CERTIFICATE-----"""
