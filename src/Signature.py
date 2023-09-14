from Firmware import Firmware
from Certificate_Chain import Certificate_Chain
from cryptography.hazmat.primitives.hashes import MD5, SHA256, SHAKE256
from cryptography.hazmat.primitives import hashes
from typing import Union
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.asymmetric.ed448 import Ed448PrivateKey
from JSON import JSON
from Utility_Functions import *


SUPPORTED_PRIVATE_KEYS = Union[Ed448PrivateKey, Ed25519PrivateKey]
SUPPORTED_HASH_ALGORITHMS = Union[SHA256, MD5]


class Signature:
    private_key = None
    sign_algorithm = None
    hash_algorithm = None
    firmware = None
    json = None
    certificate_chain = None
    digest = None
    data = None

    def __init__(self, sign_algorithm, hash_algorithm: SUPPORTED_HASH_ALGORITHMS, private_key: SUPPORTED_PRIVATE_KEYS,  firmware: Firmware, json: JSON, certificate_chain: Certificate_Chain) -> None:
        self.private_key = private_key
        self.sign_algorithm = sign_algorithm
        self.hash_algorithm = hash_algorithm
        self.firmware = firmware
        self.certificate_chain = certificate_chain
        self.json = json

        # calculate hash
        self.digest = self.__CalculateHash(
            hash_algorithm, firmware, json, certificate_chain)

        # Sign the hash bytes
        self.data = self.__SignDigest(self.digest)

        assert (self.private_key
                and self.sign_algorithm
                and self.hash_algorithm
                and self.firmware
                and self.certificate_chain
                and self.json
                and self.digest
                and self.data)
        pass

    def __CalculateHash(self, hash_algorithm: SUPPORTED_HASH_ALGORITHMS, firmware: Firmware, json: JSON, certificate_chain: Certificate_Chain):

        digest = hashes.Hash(hash_algorithm)
        digest.update(firmware.data)
        digest.update(json.__str__().encode("utf-8"))
        digest.update(certificate_chain.data)
        return digest.finalize()

    def __SignDigest(self, digest):
        assert digest

        return self.private_key.sign(digest)

    def SaveFile(self, path) -> None:
        f = open(path, "w")
        f.write(self.__str__())
        f.close()

        print("Signature file saved")
        return

    pass
