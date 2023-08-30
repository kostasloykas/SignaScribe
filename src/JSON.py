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

        assert self.arguments != None and self.firmware != None

    def SaveFile(self) -> None:
        DEBUG(os.getcwd())
        new_directory = "./build"

        # Check if the directory doesn't exist
        if not os.path.exists(new_directory):
            # Create the directory
            os.makedirs(new_directory)

        # f = open(os.getcwd() + "/build/informations.json", "w")
        f = open("./build/informations.json", "w")
        f.write(self.__str__())
        f.close()
        return

    def __str__(self) -> str:
        return json.dumps(
            {"manifest_id": self.arguments.manifest_id, "vendor_id": self.arguments.vendor_id,
             "product_id": self.arguments.product_id, "timestamp": self.arguments.timestamp,
             "hash_type": self.arguments.hash_type, "owner_id": self.arguments.owner_id,
             "sign_algorithm": self.arguments.sign_algorithm, "firmware_size": self.firmware.size,
             "firmware_type": self.firmware.type}, indent=4)

    pass
