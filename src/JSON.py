from Arguments import Arguments
from Firmware import Firmware
import json
from OpenSSL import crypto
from Utility_Functions import *


class JSON:
    arguments = None
    firmware = None
    owner_certificate = None

    def __init__(self, arguments: Arguments, firmware: Firmware, owner_certificate: crypto.X509) -> None:
        self.arguments = arguments
        self.firmware = firmware
        self.owner_certificate = owner_certificate

        assert self.arguments and self.firmware and self.owner_certificate

    def SaveFile(self, path) -> None:
        f = open(path, "w")
        f.write(self.__str__())
        f.close()

        print("JSON file saved")
        return

    def __str__(self) -> str:
        # FIXME: common name
        return json.dumps(
            {"manifest_version": self.arguments.manifest_version, "common_name": self.owner_certificate.get_subject().CN,
             "vendor_id": self.arguments.vendor_id,
             "product_id": self.arguments.product_id, "timestamp": self.arguments.timestamp,
             "hash_algorithm": self.arguments.hash_algorithm, "sign_algorithm": self.arguments.sign_algorithm,
             "firmware_size": self.firmware.size, "firmware_type": self.firmware.type}, indent=4)

    pass
