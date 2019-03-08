import React, { Component } from 'react';
import CertificatesService from './CertificatesService';

const certificatesService = new CertificatesService();

class CertificatesList extends Component {

    constructor(props) {
        super(props);
        this.state = {
            certificates: [],
            nextPageURL: ''
        };
        this.nextPage = this.nextPage.bind(this);
        this.handleDelete = this.handleDelete.bind(this);
    }


    componentDidMount() {
        var self = this;
        certificatesService.getCertificates().then(function (result) {
            self.setState({ certificates: result.results, nextPageURL: result.next })
        });
    }

    handleDelete(e, pk) {
        var self = this;
        certificatesService.deleteCertificate({ pk: pk }).then(() => {
            var newArr = self.state.certificates.filter(function (obj) {
                return obj.pk !== pk;
            });
            self.setState({ certificates: newArr })
        });
    }

    nextPage() {
        var self = this;
        certificatesService.getCertificatessByURL(this.state.nextPageURL).then((result) => {
            self.setState({ certificates: result.data, nextPageURL: result.nextlink })
        });
    }

    render() {

        return (
            <div className="certificates--list">
                <table className="table">
                    <thead key="thead">
                        <tr>
                            <th>CN</th>
                            <th>Subject</th>
                            <th>Issuer</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.state.certificates.map(c =>
                            <tr key={c.id}>
                                <td>{c.cn}  </td>
                                <td>{c.subject}</td>
                                <td>{c.issuer}</td>
                                <td>
                                    <button onClick={(e) => this.handleDelete(e, c.pk)}> Delete</button>
                                    <a href={"/certificates/" + c.pk}> Update</a>
                                </td>
                            </tr>)}
                    </tbody>
                </table>
                <button className="btn btn-primary" onClick={this.nextPage}>Next</button>
            </div>
        );
    }
}
export default CertificatesList
