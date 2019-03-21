from http import HTTPStatus
from http.client import responses
import json

import requests

CERT = """
-----BEGIN CERTIFICATE-----
MIIDeDCCAmCgAwIBAgIJAKkK3/imJk/0MA0GCSqGSIb3DQEBCwUAMFExCzAJBgNV
BAYTAkdCMQ8wDQYDVQQIDAZTdGFmZnMxDjAMBgNVBAcMBVN0b2tlMQwwCgYDVQQK
DANSS0MxEzARBgNVBAMMCmNlcnRocS5jb20wHhcNMTkwMjE3MTAyNzE3WhcNMjAw
MjE3MTAyNzE3WjBRMQswCQYDVQQGEwJHQjEPMA0GA1UECAwGU3RhZmZzMQ4wDAYD
VQQHDAVTdG9rZTEMMAoGA1UECgwDUktDMRMwEQYDVQQDDApjZXJ0aHEuY29tMIIB
IjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsYol53wZyEoWYw0fH7HqM7qp
EnQ7Qcugoac06AQ5TYIMcEYZQS8wzgC5t212iDkBxgG5TbH/xsgg+BQxxLYv0s0Q
aX9h+B48A2sjjyOL6zxf1DVR/oLPUn4jOXVmR4P1U1GGaIjZcJQsdoFII+Yuzamh
svfGxp+KSeyqCP59pbn/7c48fWGuhbaN/NqOIhviIbFqq2ClPw6CG1fR3m41u+cb
uPPrWa6Wa9dx0o2F0+UBDRekgkGLXYQYp02xtG/w3XV5kDcxFu5tp4MyCc7Lpiup
wHwe1aSsoUzUHdno0BTFLCH7aqm4AQKbp4UumUduxbdFVbXAuC90zO1Ob4xY/QID
AQABo1MwUTAdBgNVHQ4EFgQUPOLL1BamOTTp7FBiw8ioH5yYnhswHwYDVR0jBBgw
FoAUPOLL1BamOTTp7FBiw8ioH5yYnhswDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG
9w0BAQsFAAOCAQEAZ/WPr3JWzSDYOMB1WeBjpMrKtBOF5jnryU0bnkClNAX7p8AV
vrvN3d7WxOpTzoC5zNBrunzgtq33l6loSPPS10Sin8UJ82zWdKU4ZoIHDXj9YyIZ
rINHA0VGGc9iISw8dONDQcb9JlV7ainUYufMPfGaAlsJRA3Le5fFDhMo46jTrJSm
0nlYyse2M8W73EqtT8KhseABemZJoneZAm8YnHaN+0XQ83Rysm5gI0yAWXYgHx0C
tnKuAkVyBlUuoSkodkSCHFje0AGq9SCxUSdhlIgabiXbMu6CJaZIUnu10fJT8Eec
/MFK4XWv3VRL+H1Q3x6tWs+KHyD/jrHokjhlWg==
-----END CERTIFICATE-----"""

hostname='localhost'
port='8000'

url = f'http://{hostname}:{port}/api/v1/certificates'
r = requests.post(url, {'pem_data': CERT})
if r.status_code == HTTPStatus.CREATED:
    print("certificate added")
else:
    print(f"Unexpected status_code: {r.status_code} {responses[r.status_code]}")


