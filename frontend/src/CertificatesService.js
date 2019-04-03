import axios from 'axios';
const hostname = 'certhq-stage.eu-west-2.elasticbeanstalk.com'
const port = '80'
const API_URL = `http://${hostname}:${port}`;

export default class CertificatesService{

    getCertificates() {
        const url = `${API_URL}/api/v1/certificates`;
        return axios.get(url).then(response => response.data);
    }  
    getCertificatesByURL(link){
        return axios.get(link).then(response => response.data);
    }
    getCertificate(pk) {
        const url = `${API_URL}/api/v1/certificates/${pk}`;
        return axios.get(url).then(response => response.data);
    }
    deleteCertificate(certificate){
        const url = `${API_URL}/api/v1/certificates/${certificate.pk}`;
        return axios.delete(url);
    }
    createCertificate(certificate){
        const url = `${API_URL}/api/v1/certificates/`;
        return axios.post(url,certificate);
    }
    updateCertificate(certificate){
        const url = `${API_URL}/api/v1/certificates/${certificate.pk}`;
        return axios.put(url,certificate);
    }
}
