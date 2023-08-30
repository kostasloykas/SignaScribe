from JSON import JSON
from Certificate import Certificate
from Firmware import Firmware
from Signature import Signature


class Zip:
    firmware = None
    signature = None
    json = None
    certificate = None

    def __init__(self, firmware: Firmware, signature: Signature, certificate: Certificate, json: JSON) -> None:
        assert firmware and signature and certificate and json

        self.signature = signature
        self.json = json
        self.firmware = firmware
        self.certificate = certificate

        assert self.firmware and self.signature and self.certificate and self.json
        pass

    # TODO: SaveZipFile
    def SaveZipFile():
        return

    pass
