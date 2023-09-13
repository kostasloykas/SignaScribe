from Firmware import Firmware
from Certificate_Chain import Certificate_Chain
from Signature import Signature
import os


class Saver:

    folder_name = "TilergatisFiles"

    def __init__(self, firmware: Firmware, json, certificate_chain: Certificate_Chain, signature: Signature) -> None:
        pass

    def SaveAllFiles(self):
        self.path = os.getcwd()
        return
    pass
