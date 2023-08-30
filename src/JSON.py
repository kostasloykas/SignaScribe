from typing import Any
from Arguments import Arguments
from Certificate import Certificate


class JSON:
    arguments = None
    certificate = None

    def __init__(self, arguments: Arguments, certificate: Certificate) -> None:
        self.arguments = arguments
        self.certificate = certificate

        assert self.arguments != None and self.certificate != None

    def CreateJSON(self) -> str:
        json_file = json.dumps(
            {"manifest_id": self.manifest_id, "vendor_id": self.vendor_id,
             "product_id": self.product_id, "timestamp": self.timestamp,
             "hash_type": self.hash_type, "owner_id": self.owner_id, "Sign Algorithm": self.sign_algorithm})

        return json_file

    # FIXME: __str__ JSON  class
    def __str__(self) -> str:
        return ""

    pass
