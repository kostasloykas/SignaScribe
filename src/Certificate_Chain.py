from cryptography.hazmat.primitives.asymmetric import ec
from Utility_Functions import *
from cryptography.x509.oid import AttributeOID, NameOID
from cryptography.hazmat.primitives import serialization
from datetime import datetime
from Arguments import *
from cryptography.hazmat.backends import default_backend
from OpenSSL import crypto
import certifi


class Certificate_Chain:

    data = None
    type_of_public_key = None
    public_key = None
    root = None
    intermediate = None
    certificate = None
    certificates = []
    SUPPORTED_PUBLIC_KEY_ALGORITHMS = [ec.EllipticCurvePublicKey]

    def __init__(self, arguments: Arguments) -> None:
        self.data = arguments.certificate_chain.read()

        # take root,intermidiate and owner certificates from file
        self.certificates = self.__DistinguishCertificates(self.data)

        self.certificate = self.__TakeOwnerCertificate(self.certificates)
        self.intermediate = self.__TakeIntermediateCertificate(
            self.certificates)
        self.root = self.__TakeRootCertificate(self.certificates)

        if self.__CertificateChainIsNotValid(self.certificate, self.intermediate, self.root):
            ERROR("Certificate chain validation failed")

        if not self.__ValidAtThisTime():
            ERROR("The certificate isn't valid")

        # Take the type of public key from certificate
        self.public_key = self.certificate.get_pubkey()
        self.type_of_public_key = self.public_key.type()
        # TODO: public key type must be in supoorted algorithms

        # if not self.type_of_public_key in self.SUPPORTED_PUBLIC_KEY_ALGORITHMS:
        #     ERROR("Type of public key doesn't supported")

        # # check if public key its the same with certificate
        # if not self.__ContainsThePublicKey(arguments.public_key):
        #     ERROR("Public key is not the same with certificate's public key")

        # # check if the certificate contains owner's id
        # if not self.__ContainsOwnerID(arguments.owner_id):
        #     ERROR("The certificate doesn't contains owner's id")

        assert self.certificates and self.data and self.certificate and self.intermediate and self.root

    def __DistinguishCertificates(self, data) -> []:
        certificates = []

        for cert in data.split(b'-----END CERTIFICATE-----\n'):
            # Re-add the "-----END CERTIFICATE-----" line
            if (not b'-----END CERTIFICATE-----' in cert):
                cert += b'-----END CERTIFICATE-----\n'

            certificates.append(cert)
        return certificates

    def __CertificateChainIsNotValid(self, certificate, intermediate, root: crypto.X509) -> bool:
        assert certificate and intermediate and root

        # load trusted certificates
        store = crypto.X509Store()
        for trusted_cert in self.__LoadTrustedCertificates(certifi.where()):
            store.add_cert(trusted_cert)

        # Check the indermidiate chain certificates before adding it to the store
        store_ctx = crypto.X509StoreContext(
            store, intermediate)

        # verify intermidiate certificate
        try:
            store_ctx.verify_certificate()
        except:
            return True

        # add intermidiate certificate as trusted
        store.add_cert(intermediate)
        store_ctx = crypto.X509StoreContext(
            store, certificate)

        # verify owner certificate
        try:
            store_ctx.verify_certificate()
        except:
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
            except crypto.Error as e:
                # Handle any errors in certificate loading
                print(f"Error loading certificate: {e}")

        return trusted_certificates

    def __TakeOwnerCertificate(self, certificates) -> crypto.X509:
        return crypto.load_certificate(
            crypto.FILETYPE_PEM, certificates[0])

    def __TakeIntermediateCertificate(self, certificates) -> crypto.X509:
        return crypto.load_certificate(
            crypto.FILETYPE_PEM, certificates[1])

    def __TakeRootCertificate(self, certificates) -> crypto.X509:
        return crypto.load_certificate(
            crypto.FILETYPE_PEM, certificates[2])

    def __ContainsOwnerID(self, owner_id) -> bool:
        common_name = self.certificate.subject.get_attributes_for_oid(
            NameOID.COMMON_NAME)[0].value

        if common_name != owner_id:
            return False

        return True

    def __ContainsThePublicKey(self, argument_public_key) -> bool:
        assert self.public_key != None and argument_public_key != None

        # convert certificate's public key into bytes
        bytes_public_key = self.public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                        format=serialization.PublicFormat.SubjectPublicKeyInfo)

        if (bytes_public_key != argument_public_key):
            return False

        return True

    def __ValidAtThisTime(self) -> bool:
        date_format = "%Y%m%d%H%M%SZ"  # SSL certificate date format (UTC)
        not_valid_after = datetime.strptime(
            self.certificate.get_notAfter().decode('utf-8'), date_format)
        not_valid_before = datetime.strptime(
            self.certificate.get_notBefore().decode('utf-8'), date_format)

        if datetime.now() > not_valid_after or datetime.now() < not_valid_before:
            return False  # the certificate isn't in valid timestamp

        return True  # the certificate is in valid timestamp

    pass
