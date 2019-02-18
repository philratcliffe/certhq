
import ssl
conn = ssl.create_connection(('tls-v1-0.badssl.com', 1010))
context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
sock = context.wrap_socket(conn, server_hostname='tls-v1-0.badssl.com')
der_certificate = sock.getpeercert(binary_form=True)
pem_certificate = ssl.DER_cert_to_PEM_cert(der_certificate)
print(pem_certificate)


