from Firmware import Firmware
from Certificate_Chain import Certificate_Chain
from Signature import Signature
from Zip import Zip
import os


class Saver:

    folder_name = "TilergatisFiles"

    def __init__(self, firmware: Firmware, json, certificate_chain: Certificate_Chain, signature: Signature, zip) -> None:
        pass

    def SaveAllFilesIntoZip(self, zip: Zip):
        self.path = os.getcwd()

        # delete all unneccecery files
        return
    pass
