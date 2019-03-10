import json

import requests

url = 'http://localhost:8000/api/v1/certificates'
r = requests.get(url)
d = json.loads(r.text)
results = d['results']

for result in results:
    print('id:', result['id'])
    print('cn:', result['cn'])
    print('subject:', result['subject'])
    print('sha256_fingerprint:', result['sha256_fingerprint'])
    print('pem_data:', result['pem_data'])
