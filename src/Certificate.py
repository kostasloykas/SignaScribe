from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import rsa, ec
from Utility_Functions import *
from cryptography.x509.oid import AttributeOID, NameOID
from cryptography.hazmat.primitives import serialization
from datetime import datetime
from Arguments import *
from cryptography.hazmat.backends import default_backend
from OpenSSL import crypto


class Certificate:

    data = None
    type_of_public_key = None
    public_key = None
    root = None
    intermediate = None
    certificate = None
    certificates = []

    # FIXME: SUPPORTED_PUBLIC_KEY_ALGORITHMS = [ec.EllipticCurvePublicKey]
    SUPPORTED_PUBLIC_KEY_ALGORITHMS = [ec.EllipticCurvePublicKey]

    def __init__(self, arguments: Arguments) -> None:
        self.data = arguments.certificate.read()

        # distinguish certificates
        for cert in self.data.split(b'-----END CERTIFICATE-----\n'):
            # Re-add the "-----END CERTIFICATE-----" line
            if (not b'-----END CERTIFICATE-----' in cert):
                cert += b'-----END CERTIFICATE-----\n'

            self.certificates.append(cert)

        self.certificate = self.__TakeOwnerCertificate(self.certificates)
        self.intermediate = self.__TakeIntermediateCertificate(
            self.certificates)
        self.root = self.__TakeRootCertificate(self.certificates)

        if self.__CertificateChainIsNotValid(self.certificate, self.intermediate, self.root):
            ERROR("Certificate chain validation failed")

        # # TODO: __VerifyTheSignatureOfCA
        # if not self.__VerifyTheSignatureOfCA():
        #     ERROR("Certificate validation failed")
        # else:
        #     print("Certificate validation success")

        # if not self.__ValidAtThisTime():
        #     ERROR("The certificate isn't valid")

        # # Take the type of public key from certificate
        # self.public_key = self.certificate.public_key()
        # self.type_of_public_key = self.__TypeOfPublicKey(self.public_key)

        # if not self.type_of_public_key in self.SUPPORTED_PUBLIC_KEY_ALGORITHMS:
        #     ERROR("Type of public key doesn't supported")

        # # check if public key its the same with certificate
        # if not self.__ContainsThePublicKey(arguments.public_key):
        #     ERROR("Public key is not the same with certificate's public key")

        # # check if the certificate contains owner's id
        # if not self.__ContainsOwnerID(arguments.owner_id):
        #     ERROR("The certificate doesn't contains owner's id")

        # assert self.certificate and self.public_key and self.data

    def __CertificateChainIsNotValid(self, certificate, intermediate, root) -> bool:
        assert certificate and intermediate and root

        crypto.X509()
        store = crypto.X509Store()
        store.add_cert(root)

        DEBUG(intermediate)
        # Check the chain certificate before adding it to the store
        store_ctx = crypto.X509StoreContext(store, intermediate)
        store_ctx.verify_certificate()

        return True

    def __TypeOfPublicKey(self, public_key) -> ec.EllipticCurvePublicKey:

        for type in self.SUPPORTED_PUBLIC_KEY_ALGORITHMS:
            if isinstance(public_key, type):
                return type

        return None

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
        not_valid_after = self.certificate.not_valid_after
        not_valid_before = self.certificate.not_valid_before

        if datetime.now() > not_valid_after or datetime.now() < not_valid_before:
            return False  # the certificate isn't in valid timestamp

        return True  # the certificate is in valid timestamp

    pass
