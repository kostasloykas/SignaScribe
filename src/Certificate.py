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

    # FIXME: SUPPORTED_PUBLIC_KEY_ALGORITHMS = [ec.EllipticCurvePublicKey]
    SUPPORTED_PUBLIC_KEY_ALGORITHMS = [ec.EllipticCurvePublicKey]

    def __init__(self, arguments: Arguments) -> None:
        self.data = arguments.certificate.read()
        # TODO: self.__TakeRootCertificate(self.data)
        # TODO: self.__TakeIntermediateCertificates(self.data)
        self.certificate = self.__TakeCertificate(self.data)

        # TODO: __VerifyTheSignatureOfCA
        if not self.__VerifyTheSignatureOfCA():
            ERROR("Certificate validation failed")
        else:
            print("Certificate validation success")

        if not self.__ValidAtThisTime():
            ERROR("The certificate isn't valid")

        # Take the type of public key from certificate
        self.public_key = self.certificate.public_key()
        self.type_of_public_key = self.__TypeOfPublicKey(self.public_key)

        if not self.type_of_public_key in self.SUPPORTED_PUBLIC_KEY_ALGORITHMS:
            ERROR("Type of public key doesn't supported")

        # check if public key its the same with certificate
        if not self.__ContainsThePublicKey(arguments.public_key):
            ERROR("Public key is not the same with certificate's public key")

        # check if the certificate contains owner's id
        if not self.__ContainsOwnerID(arguments.owner_id):
            ERROR("The certificate doesn't contains owner's id")

        assert self.certificate and self.public_key and self.data

    def __TypeOfPublicKey(self, public_key) -> ec.EllipticCurvePublicKey:

        for type in self.SUPPORTED_PUBLIC_KEY_ALGORITHMS:
            if isinstance(public_key, type):
                return type

        return None

    def __TakeCertificate(self, certificate) -> x509.Certificate:
        return x509.load_pem_x509_certificate(certificate, default_backend())

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

    # TODO: VerifyTheSignatureOfCA
    def __VerifyTheSignatureOfCA(self) -> bool:
        store = crypto.X509Store()
        store.add_cert()

        # root
        # intermmidiate
        # client certificate

        return False

    def __ValidAtThisTime(self) -> bool:
        not_valid_after = self.certificate.not_valid_after
        not_valid_before = self.certificate.not_valid_before

        if datetime.now() > not_valid_after or datetime.now() < not_valid_before:
            return False  # the certificate isn't in valid timestamp

        return True  # the certificate is in valid timestamp

    pass
