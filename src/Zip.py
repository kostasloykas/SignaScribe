from JSON import JSON
from Certificate import Certificate
from Firmware import Firmware
from Signature import Signature
import os
from zipfile import ZipFile


class Zip:
    firmware = None
    signature = None
    json = None
    certificate = None
    path = "./build/tilergatis.zip"

    def __init__(self, firmware: Firmware, signature: Signature, certificate: Certificate, json: JSON) -> None:
        assert firmware and signature and certificate and json

        self.signature = signature
        self.json = json
        self.firmware = firmware
        self.certificate = certificate

        assert self.firmware and self.signature and self.certificate and self.json

    def __CreateBuildFolder(self):
        new_directory = "./build"

        # Check if the directory doesn't exist
        if not os.path.exists(new_directory):
            # Create the directory
            os.makedirs(new_directory)

        return

    def SaveFile(self) -> None:
        self.__CreateBuildFolder()

        file_paths = [self.json.path]

        # Create a new ZIP archive and add files to it
        with ZipFile(self.path, 'w') as zip:
            for file_path in file_paths:
                # Add the file to the ZIP archive
                zip.write(file_path)

        zip.close()
        print("Zip file saved")
        return

    pass
