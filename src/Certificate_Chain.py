from cryptography.hazmat.primitives.asymmetric import ec
from Utility_Functions import *
from cryptography.x509.oid import AttributeOID, NameOID
from cryptography.hazmat.primitives import serialization
from datetime import datetime
from Arguments import *
from OpenSSL import crypto
import certifi
from typing import List


class Certificate_Chain:

    data = None
    root = None
    intermediate_certificates = None
    owner_certificate = None
    certificates = []

    def __init__(self, arguments: Arguments) -> None:
        self.data = arguments.certificate_chain.read()

        # all the certificates
        self.certificates = self.__DistinguishCertificates(self.data)

        if len(self.certificates) < 1:
            ERROR("Certificate file must have at least 1 certificate")

        # take owner certificate
        self.owner_certificate = self.__TakeOwnerCertificate(self.certificates)

        # If chain has intermediate certificate extract them
        if len(self.certificates) >= 3:
            # take intermmediate certificates
            self.intermediate_certificates = self.__TakeIntermediateCertificates(
                self.certificates)

            # # take root certificate
            # self.root = self.__TakeRootCertificate(self.certificates)
        # else:
        #     # take only root certificate
        #     self.root = self.__TakeRootCertificate(self.certificates)

        if self.__CertificateChainIsNotValid(self.owner_certificate, self.intermediate_certificates):
            ERROR("Certificate chain validation failed")

        if not self.__ValidAtThisTime():
            ERROR("The certificate isn't valid")

        # Take the type of public key from certificate
        self.public_key = self.owner_certificate.get_pubkey()
        self.type_of_public_key = self.public_key.type()

        assert self.certificates and self.data and self.owner_certificate and self.intermediate_certificates

    def __DistinguishCertificates(self, data) -> []:
        certificates = []

        for cert in data.split(b'-----END CERTIFICATE-----\n'):
            # Re-add the "-----END CERTIFICATE-----" line
            if (b'-----BEGIN CERTIFICATE-----' in cert and not b'-----END CERTIFICATE-----' in cert):
                cert += b'-----END CERTIFICATE-----\n'
                certificates.append(cert)

        return certificates

    def __CertificateChainIsNotValid(self, owner_certificate: crypto.X509, intermediate_certificates: List[crypto.X509]) -> bool:
        assert owner_certificate and intermediate_certificates

        # load trusted certificates and add them to x509 store
        store = crypto.X509Store()
        for trusted_cert in self.__LoadTrustedCertificates(certifi.where()):
            store.add_cert(trusted_cert)

        # Check the indermediate chain certificates before adding it to the store
        intermediate_certificates.reverse()

        for cert in intermediate_certificates:
            store_ctx = crypto.X509StoreContext(
                store, cert)

            # verify chain
            try:
                store_ctx.verify_certificate()
                store.add_cert(cert)
            except:
                print("ERROR: Couldn't verify intermediate certificate chain")
                return True

        # verify owner certificate
        store_ctx = crypto.X509StoreContext(
            store, owner_certificate)

        try:
            store_ctx.verify_certificate()
        except:
            print("ERROR: Verify owner certificate")
            return True

        return False

    def __LoadTrustedCertificates(self, path):
        trusted_certificates = []

        # Load the CA certificates from the bundle
        with open(path, 'rb') as ca_file:
            ca_bundle = ca_file.read()

        # Create a list to store X509 certificate objects
        all_certificates = self.__DistinguishCertificates(ca_bundle)
        all_certificates.pop(len(all_certificates)-1)

        # Parse and load each certificate in the bundle
        for cert in all_certificates:
            try:

                x509_cert = crypto.load_certificate(
                    crypto.FILETYPE_PEM, cert)
                trusted_certificates.append(x509_cert)
            except:
                # Handle any errors in certificate loading
                print(f"Error loading trusted certificate")

        return trusted_certificates

    def __TakeOwnerCertificate(self, certificates) -> crypto.X509:
        return crypto.load_certificate(
            crypto.FILETYPE_PEM, certificates[0])

    def __TakeIntermediateCertificates(self, certificates) -> List[crypto.X509]:
        intermediate_certificates = []

        # load intermmediate certificates and add them to the list
        for cert in certificates[1:len(certificates)-1]:
            intermediate_certificates.append(
                crypto.load_certificate(crypto.FILETYPE_PEM, cert))

        assert len(intermediate_certificates) != 0
        return intermediate_certificates

    def __TakeRootCertificate(self, certificates) -> crypto.X509:
        return crypto.load_certificate(
            crypto.FILETYPE_PEM, certificates[len(certificates)-1])

    def __ValidAtThisTime(self) -> bool:
        date_format = "%Y%m%d%H%M%SZ"  # SSL certificate date format (UTC)
        not_valid_after = datetime.strptime(
            self.owner_certificate.get_notAfter().decode('utf-8'), date_format)
        not_valid_before = datetime.strptime(
            self.owner_certificate.get_notBefore().decode('utf-8'), date_format)

        if datetime.now() > not_valid_after or datetime.now() < not_valid_before:
            return False  # the certificate isn't in valid timestamp

        return True  # the certificate is in valid timestamp

    pass
