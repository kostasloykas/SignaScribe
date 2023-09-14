import argparse
from datetime import datetime, timedelta
from Utility_Functions import *


class Arguments:

    firmware = None
    manifest_version = None
    vendor_id = None
    product_id = None
    timestamp = None
    hash_algorithm = None
    certificate_chain = None
    sign_algorithm = None

    def ParseArguments(self) -> None:

        self.parser = argparse.ArgumentParser(prog='SignaScribe')

        # define manifest fields
        self.parser.add_argument('-m', '--manifest_version',
                                 type=int, choices=[0], required=True, help="Manifest version")
        self.parser.add_argument('-f', '--firmware', type=argparse.FileType("rb"), required=True,
                                 help="The firmware that will be signed. Accepts only hex,bin and zip files.")
        self.parser.add_argument('-c', '--certificate_chain', type=argparse.FileType("rb"), required=True,
                                 help="The certificate chain in .crt format")
        self.parser.add_argument('-ha', '--hash_algorithm', type=str, choices=["sha256"], required=True,
                                 help="The hash algorithm will be used")
        self.parser.add_argument(
            '-pi', '--product_id', type=str, required=True, help="The device's product id in hex format")
        self.parser.add_argument(
            '-vi', '--vendor_id', type=str, required=True, help="The device's vendor id in hex format")
        self.parser.add_argument('-sa', '--sign_algorithm',
                                 type=str, required=True, choices=["eddsa448", "eddsa25519"], help="Choose which digital sign algorithm you want to use")

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

            # manifest version
            self.manifest_version = arguments.manifest_version

            # read file
            self.firmware = arguments.firmware

            # sign algorithm
            self.sign_algorithm = arguments.sign_algorithm

            # hash algorithm
            self.hash_algorithm = arguments.hash_algorithm

            # certificate
            self.certificate_chain = arguments.certificate_chain

        except Exception as ex:
            ERROR(ex)

        assert (self.firmware and
                self.manifest_version != None and
                self.vendor_id and
                self.product_id and
                self.timestamp and
                self.hash_algorithm and
                self.certificate_chain and
                self.sign_algorithm)
        return

    def __str__(self) -> str:
        return f"Argument object: manifest id={self.manifest_version} , vendor id={self.vendor_id} , product id={self.product_id} , timestamp={self.timestamp}  , hash type={self.hash_algorithm} "
