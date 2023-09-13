from typing import Any
from Arguments import Arguments
from Firmware import Firmware
import json
import os
from Utility_Functions import *


class JSON:
    arguments = None
    firmware = None
    path = "informations.json"

    def __init__(self, arguments: Arguments, firmware: Firmware) -> None:
        self.arguments = arguments
        self.firmware = firmware

        DEBUG("JSON file: ", self)
        assert self.arguments != None and self.firmware != None

    def SaveFile(self) -> None:
        f = open(self.path, "w")
        f.write(self.__str__())
        f.close()

        print("JSON file saved")
        return

    def __str__(self) -> str:
        return json.dumps(
            {"manifest_id": self.arguments.manifest_version, "vendor_id": self.arguments.vendor_id,
             "product_id": self.arguments.product_id, "timestamp": self.arguments.timestamp,
             "hash_type": self.arguments.hash_type, "owner_id": self.arguments.owner_id,
             "sign_algorithm": self.arguments.sign_algorithm, "firmware_size": self.firmware.size,
             "firmware_type": self.firmware.type}, indent=4)

    pass
