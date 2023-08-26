from cryptography import x509
from Utility_Functions import *


class Certificate:
    data = None
    certificate = None

    def __init__(self, data) -> None:
        self.data = data
        self.certificate = self.__TakeCertificate()

        assert (data != None and self.certificate != None)

    def __TakeCertificate(self) -> x509.Certificate:
        return x509.load_pem_x509_certificate(self.data)

    pass
