from cryptography import x509
from Utility_Functions import *
from cryptography.x509.oid import AttributeOID, NameOID
from cryptography.hazmat.primitives import serialization
from datetime import datetime
from Arguments import *


class Certificate:
    certificate = None
    type_of_public_key = None
    public_key = None

    def __init__(self, arguments: Arguments) -> None:
        self.certificate = self.__TakeCertificate(arguments.certificate)

        if not self.__ValidAtThisTime():
            ERROR("The certificate isn't valid")

        # check if owner id its the same with certificate
        # check if public key its the same with certificate

        assert (self.certificate != None)

    def __TakeCertificate(self, certificate) -> x509.Certificate:
        return x509.load_pem_x509_certificate(certificate)

    # TODO: IsTrustedCA
    def __IsFromTrustedCA(self) -> bool:
        return

    # TODO: IsValidAtThisTime
    def __ValidAtThisTime(self) -> bool:
        not_valid_after = self.certificate.not_valid_after
        not_valid_before = self.certificate.not_valid_before

        if datetime.now() > not_valid_after or datetime.now() < not_valid_before:
            return False  # the certificate isn't in valid timestamp

        return True  # the certificate is in valid timestamp

    pass
