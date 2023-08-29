import argparse
from datetime import datetime, timedelta
from Utility_Functions import *
import json
import magic


class Arguments:

    firmware = None
    manifest_id = None
    vendor_id = None
    product_id = None
    timestamp = None
    hash_type = None
    owner_id = None
    certificate = None
    SUPPORTED_EXTENTIONS = ["hex", "bin", "zip"]

    def ParseArguments(self) -> None:

        self.parser = argparse.ArgumentParser(prog='SignaScribe')

        # define manifest fields
        self.parser.add_argument('-mi', '--manifest_id',
                                 type=int, required=True, help="Manifest ID")
        self.parser.add_argument('-f', '--firmware', type=argparse.FileType("rb"), required=True,
                                 help="The firmware")
        self.parser.add_argument('-c', '--certificate', type=argparse.FileType("rb"), required=True,
                                 help="The certificate of owner")
        self.parser.add_argument('-ht', '--hash_type', type=str, choices=["sha256"], required=True,
                                 help="The hash algorithm that will be used")
        self.parser.add_argument(
            '-pi', '--product_id', type=str, required=True, help="The device's product id in hex format")
        self.parser.add_argument(
            '-vi', '--vendor_id', type=str, required=True, help="The device's vendor id in hex format")
        self.parser.add_argument('-p', '--public_key', type=argparse.FileType("rb"), required=True,
                                 help="Public key file")
        self.parser.add_argument('-sa', '--sign_algorithm',
                                 type=str, required=True, choices=["eddsa"], help="Choose which digital sign algorithm you want to use")

        # parse arguments
        arguments = self.parser.parse_args()

        self.CheckArguments(arguments)
        return

    def CheckArguments(self, arguments) -> None:

        try:

            # timestamp
            self.timestamp = str(datetime.now())

            # product id
            self.product_id = int(arguments.product_id, 16)

            # vendor id
            self.vendor_id = int(arguments.vendor_id, 16)

            # manifest id
            self.manifest_id = arguments.manifest_id

            # read file
            self.firmware = arguments.firmware.read()
            self.__CheckFirmwareExtention(arguments.firmware.name)

            # hash type
            self.hash_type = arguments.hash_type

            self.certificate = arguments.certificate.read()

        except Exception as ex:
            ERROR(ex)

        assert (self.firmware != None and
                self.manifest_id != None and
                self.vendor_id != None and
                self.product_id != None and
                self.firmware != None and
                self.timestamp != None and
                self.hash_type != None and
                self.certificate != None)
        return

    def CreateJSON(self) -> str:
        json_file = json.dumps(
            {"manifest_id": self.manifest_id, "vendor_id": self.vendor_id,
             "product_id": self.product_id, "timestamp": self.timestamp, "hash_type": self.hash_type})

        return json_file

    def __CheckFirmwareExtention(self, firmware_name: str):
        mime = magic.Magic(mime=True)
        extention = mime.from_file(firmware_name)

        if not extention in self.SUPPORTED_EXTENTIONS:
            ERROR("Not supported extention of firmware file",
                  "SUPPORTED EXTENTIONS --->", self.SUPPORTED_EXTENTIONS)

    def __str__(self) -> str:
        return f"Argument object: manifest id={self.manifest_id} , vendor id={self.vendor_id} , product id={self.product_id} , timestamp={self.timestamp}  , hash type={self.hash_type} "
