from typing import Any
from Arguments import Arguments
from Firmware import Firmware
import json


class JSON:
    arguments = None
    firmware = None

    def __init__(self, arguments: Arguments, firmware: Firmware) -> None:
        self.arguments = arguments
        self.firmware = firmware

        assert self.arguments != None and self.firmware != None

    # FIXME: __str__ JSON  class
    def __str__(self) -> str:
        return json.dumps(
            {"manifest_id": self.arguments.manifest_id, "vendor_id": self.arguments.vendor_id,
             "product_id": self.arguments.product_id, "timestamp": self.arguments.timestamp,
             "hash_type": self.arguments.hash_type, "owner_id": self.arguments.owner_id,
             "Sign Algorithm": self.arguments.sign_algorithm}, indent=4)

    pass
