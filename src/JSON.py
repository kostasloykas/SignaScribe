from typing import Any
from Arguments import Arguments
from Firmware import Firmware
import json
import os
from Utility_Functions import *


class JSON:
    arguments = None
    firmware = None

    def __init__(self, arguments: Arguments, firmware: Firmware) -> None:
        self.arguments = arguments
        self.firmware = firmware

        DEBUG("JSON file: ", self)
        assert self.arguments and self.firmware

    def SaveFile(self, path) -> None:
        f = open(path, "w")
        f.write(self.__str__())
        f.close()

        print("JSON file saved")
        return

    def __str__(self) -> str:
        # FIXME: common name
        return json.dumps(
            {"manifest_version": self.arguments.manifest_version, "common_name": self.arguments.vendor_id,
             "vendor_id": self.arguments.vendor_id,
             "product_id": self.arguments.product_id, "timestamp": self.arguments.timestamp,
             "hash_type": self.arguments.hash_type, "sign_algorithm": self.arguments.sign_algorithm,
             "firmware_size": self.firmware.size, "firmware_type": self.firmware.type}, indent=4)

    pass
