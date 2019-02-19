import ssl

with open('hosts') as lines:
    for line in lines:
        line = line.strip()
        if '#' in line:
            continue
        if ':' in line:
            hostname, port = line.split(':')
            port = int(port)
        else:
            port = 443

        conn = ssl.create_connection((hostname, port))
        context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)

        # Pass the hostname for SNI servers
        sock = context.wrap_socket(conn, server_hostname=hostname)

        der_certificate = sock.getpeercert(binary_form=True)
        pem_certificate = ssl.DER_cert_to_PEM_cert(der_certificate)
        print(hostname, port)
        print(pem_certificate)


