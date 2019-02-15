import requests
import json


url = 'http://localhost:8000/api/v1/certificates'
r = requests.get(url)
list_of_results = json.loads(r.text)
for result in list_of_results:
    print(result['id'])
    print(result['cn'])
    print(result['subject'])
    print(result['sha256_fingerprint'])
    print(result['pem_data'])

