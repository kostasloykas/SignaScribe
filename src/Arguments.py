import argparse
from datetime import datetime, timedelta
from Utility_Functions import *
import json


class Arguments:

    file = None
    manifest_id = None
    vendor_id = None
    product_id = None
    timestamp = None
    hash_type = None
    owner_id = None
    certificate = None

    # FIXME: ParseArguments
    def ParseArguments(self) -> None:

        self.parser = argparse.ArgumentParser(prog='SignaScribe')

        # define manifest fields
        self.parser.add_argument('-mi', '--manifest_id',
                                 type=int, required=True, help="Manifest ID")
        self.parser.add_argument('-f', '--file', type=argparse.FileType("rb"), required=True,
                                 help="The file that will be signed")
        self.parser.add_argument('-c', '--certificate', type=argparse.FileType("rb"), required=True,
                                 help="The certificate of owner")
        self.parser.add_argument('-ht', '--hash_type', type=str, choices=["sha256"], required=True,
                                 help="The hash algorithm that will be used")
        self.parser.add_argument(
            '-pi', '--product_id', type=str, required=True, help="The device's product id in hex format")
        self.parser.add_argument(
            '-vi', '--vendor_id', type=str, required=True, help="The device's vendor id in hex format")

        # TODO: provide the options for sign algorithm
        self.parser.add_argument('-sa', '--sign_algorithm',
                                 type=str, required=True, choices=["eddsa"], help="Choose which digital sign algorithm you want to use")

        # parse arguments
        arguments = self.parser.parse_args()

        self.CheckArguments(arguments)
        return

    # FIXME: CheckArguments
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
            self.file = arguments.file.read()

            # hash type
            self.hash_type = arguments.hash_type

            self.certificate = arguments.certificate.read()
            DEBUG(self.certificate)

        except ValueError as ex:
            ERROR(ex)

        assert (self.file != None and
                self.manifest_id != None and
                self.vendor_id != None and
                self.product_id != None and
                self.file != None and
                self.timestamp != None and
                self.hash_type != None and
                self.certificate != None)
        return

    def CreateJSON(self) -> str:
        json_file = json.dumps(
            {"manifest_id": self.manifest_id, "vendor_id": self.vendor_id,
             "product_id": self.product_id, "timestamp": self.timestamp, "hash_type": self.hash_type})

        return json_file

    def __str__(self) -> str:
        return f"Argument object: manifest id={self.manifest_id} , vendor id={self.vendor_id} , product id={self.product_id} , timestamp={self.timestamp}  , hash type={self.hash_type} "
