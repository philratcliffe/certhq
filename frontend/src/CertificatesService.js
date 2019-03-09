import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class CertificatesService{

    getCertificates() {
        console.log("In getCertificates")
        const url = `${API_URL}/api/v1/certificates`;
        console.log(url)
        return axios.get(url).then(response => response.data);
    }  
    getCertificatesByURL(link){
        console.log("In getCertificatesByURL")
        console.log(link)
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
