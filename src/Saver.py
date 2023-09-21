from Firmware import Firmware
from Certificate_Chain import Certificate_Chain
from Signature import Signature
from JSON import JSON
import zipfile
import os


class Saver:

    firmware = None
    certificate_chain = None
    signature = None
    json = None

    def __init__(self, firmware: Firmware, json: JSON, certificate_chain: Certificate_Chain, signature: Signature) -> None:
        self.firmware = firmware
        self.certificate_chain = certificate_chain
        self.signature = signature
        self.json = json

        assert (self.firmware
                and self.certificate_chain
                and self.signature
                and self.json)

    def SaveAllFilesIntoZip(self, zip_name):

        # if folder doesn't exists then create one
        if not os.path.exists("build"):
            os.makedirs("build")

        with zipfile.ZipFile('build/' + zip_name, 'w') as my_zip:
            # json
            my_zip.writestr('tilergatis_manifest.json', self.json.__str__())

            # firmware
            my_zip.writestr('firmware.' + self.firmware.type,
                            self.firmware.data)

            # certificate chain
            my_zip.writestr('certificate_chain.pem',
                            self.certificate_chain.data)

            # signature
            my_zip.writestr('signature.dat', self.signature.data)

        return
    pass
