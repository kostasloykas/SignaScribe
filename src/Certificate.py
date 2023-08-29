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

        # TODO: __IsFromTrustedCA

        # check if the certificate contains owner's id
        if not self.__ContainsOwnerID(arguments.owner_id):
            ERROR("The certificate doesn't contains owner's id")

        # check if public key its the same with certificate
        if not self.__ContainsThePublicKey(arguments.public_key):
            ERROR("The certificate doesn't contains the right public key")

        assert (self.certificate != None)

    def __TakeCertificate(self, certificate) -> x509.Certificate:
        return x509.load_pem_x509_certificate(certificate)

    def __ContainsOwnerID(self, owner_id) -> bool:
        common_name = self.certificate.subject.get_attributes_for_oid(
            NameOID.COMMON_NAME)[0].value

        if common_name != owner_id:
            return False

        return True

    # TODO: __ContainsThePublicKey
    def __ContainsThePublicKey(self, public_key) -> bool:
        # use is instance gia to type tou public key

        return True

    # TODO: IsFromTrustedCA
    def __IsFromTrustedCA(self) -> bool:
        return

    # IsValidAtThisTime
    def __ValidAtThisTime(self) -> bool:
        not_valid_after = self.certificate.not_valid_after
        not_valid_before = self.certificate.not_valid_before

        if datetime.now() > not_valid_after or datetime.now() < not_valid_before:
            return False  # the certificate isn't in valid timestamp

        return True  # the certificate is in valid timestamp

    pass
