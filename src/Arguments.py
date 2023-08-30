import argparse
from datetime import datetime, timedelta
from Utility_Functions import *


class Arguments:

    firmware = None
    firmware_type = None
    manifest_id = None
    vendor_id = None
    product_id = None
    timestamp = None
    hash_type = None
    owner_id = None
    public_key = None
    certificate = None
    sign_algorithm = None

    SUPPORTED_EXTENTIONS = ["hex", "bin", "zip"]

    def ParseArguments(self) -> None:

        self.parser = argparse.ArgumentParser(prog='SignaScribe')

        # define manifest fields
        self.parser.add_argument('-mi', '--manifest_id',
                                 type=int, required=True, help="Manifest ID")
        self.parser.add_argument('-oi', '--owner_id',
                                 type=str, required=True, help="Owner ID")
        self.parser.add_argument('-f', '--firmware', type=argparse.FileType("rb"), required=True,
                                 help="The firmware that will be signed. Accepts only hex,bin and zip files.")
        self.parser.add_argument('-c', '--certificate', type=argparse.FileType("rb"), required=True,
                                 help="The certificate of owner")
        self.parser.add_argument('-ht', '--hash_type', type=str, choices=["sha256"], required=True,
                                 help="The hash algorithm that will be used")
        self.parser.add_argument(
            '-pi', '--product_id', type=str, required=True, help="The device's product id in hex format")
        self.parser.add_argument(
            '-vi', '--vendor_id', type=str, required=True, help="The device's vendor id in hex format")
        self.parser.add_argument('-p', '--public_key', type=argparse.FileType("rb"), required=True,
                                 help="Public key file in pem format")
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

            # public key
            self.public_key = arguments.public_key.read()

            # owner id
            self.owner_id = arguments.owner_id

            # product id
            self.product_id = int(arguments.product_id, 16)

            # vendor id
            self.vendor_id = int(arguments.vendor_id, 16)

            # manifest id
            self.manifest_id = arguments.manifest_id

            # read file
            self.firmware = arguments.firmware.read()

            # firmware type
            self.firmware_type = self.__TakeFirmwareExtention(
                arguments.firmware.name)

            # sign algorithm
            self.sign_algorithm = arguments.sign_algorithm

            # hash type
            self.hash_type = arguments.hash_type

            # certificate
            self.certificate = arguments.certificate.read()

        except Exception as ex:
            ERROR(ex)

        assert (self.firmware and
                self.manifest_id != None and
                self.vendor_id and
                self.product_id and
                self.timestamp and
                self.hash_type and
                self.certificate and
                self.public_key and
                self.owner_id and
                self.sign_algorithm and
                self.firmware_type)
        return

    def __TakeFirmwareExtention(self, firmware_name: str) -> str:
        extention = firmware_name.split(".").pop()

        if not extention in self.SUPPORTED_EXTENTIONS:
            ERROR("Not supported extention of firmware file",
                  "SUPPORTED EXTENTIONS --->", self.SUPPORTED_EXTENTIONS)
        return extention

    def __str__(self) -> str:
        return f"Argument object: manifest id={self.manifest_id} , vendor id={self.vendor_id} , product id={self.product_id} , timestamp={self.timestamp}  , hash type={self.hash_type} "
