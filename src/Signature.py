from Firmware import Firmware
from Certificate_Chain import Certificate_Chain
from cryptography.hazmat.primitives import hashes


class Signature:
    def __init__(self, sign_algorithm, hash_algorithm, firmware: Firmware, json, certificate_chain: Certificate_Chain) -> None:
        # FIXME: calculate hash
        # FIXME: Create Signature
        pass

    def CalculateHash(self, hash_algorithm):
        return

    def SaveFile(self, path) -> None:
        f = open(path, "w")
        f.write(self.__str__())
        f.close()

        print("Signature file saved")
        return

    pass
