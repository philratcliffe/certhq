import ssl
import socket

with open('hosts') as lines:
    for line in lines:
        line = line.strip()
        if '#' in line:
            continue
        if ':' in line:
            hostname, port = line.split(':')
            port = int(port)
        else:
            hostname = line
            port = 443

        context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        try:
            with socket.create_connection((hostname, 443)) as sock:
                with context.wrap_socket(
                        sock, server_hostname=hostname) as ssock:
                    print(ssock.version())

                    der_certificate = ssock.getpeercert(binary_form=True)
                    pem_certificate = ssl.DER_cert_to_PEM_cert(der_certificate)

                    print(hostname, port)
                    print(pem_certificate)
        except Exception as e:
            print(e)
