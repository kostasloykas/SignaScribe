from Firmware import Firmware
from Certificate_Chain import Certificate_Chain
from cryptography.hazmat.primitives.hashes import MD5, SHA256, SHAKE256
from typing import Union
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.asymmetric.ed448 import Ed448PrivateKey
from JSON import JSON


SUPPORTED_PRIVATE_KEYS = Union[Ed448PrivateKey, Ed25519PrivateKey]
SUPPORTED_HASH_ALGORITHMS = Union[SHA256, MD5]


class Signature:
    private_key = None
    sign_algorithm = None
    hash_algorithm = None
    firmware = None
    json = None
    certificate_chain = None

    def __init__(self, sign_algorithm, hash_algorithm: SUPPORTED_HASH_ALGORITHMS, private_key: SUPPORTED_PRIVATE_KEYS,  firmware: Firmware, json: JSON, certificate_chain: Certificate_Chain) -> None:
        self.private_key = private_key
        self.sign_algorithm = sign_algorithm
        self.hash_algorithm = hash_algorithm
        self.firmware = firmware
        self.certificate_chain = certificate_chain
        self.json = json

        # FIXME: calculate hash

        # FIXME: Create Signature

        assert (self.private_key
                and self.sign_algorithm
                and self.hash_algorithm
                and self.firmware
                and self.certificate_chain
                and self.json)
        pass

    def CalculateHash(self, hash_algorithm):
        hashes = {}

        return

    def SaveFile(self, path) -> None:
        f = open(path, "w")
        f.write(self.__str__())
        f.close()

        print("Signature file saved")
        return

    pass
