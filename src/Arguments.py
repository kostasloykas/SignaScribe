import argparse
from datetime import datetime, timedelta
from Utility_Functions import *
import json


class Arguments:

    file = None
    manifest_id = None
    vendor_id = None
    product_id = None
    start_date = None
    expire_date = None
    hash_type = None

    # FIXME: ParseArguments
    def ParseArguments(self) -> None:

        self.parser = argparse.ArgumentParser(prog='SignaScribe')

        # define manifest fields
        self.parser.add_argument('-mi', '--manifest_id',
                                 type=int, required=True, help="Manifest ID")
        self.parser.add_argument('-f', '--file', type=argparse.FileType("rb"), required=True,
                                 help="The file that will be signed")
        self.parser.add_argument('-ht', '--hash_type', type=str, choices=["sha256"], required=True,
                                 help="The hash algorithm that will be used")
        self.parser.add_argument(
            '-pi', '--product_id', type=str, required=True, help="The device's product id in hex format")
        self.parser.add_argument(
            '-vi', '--vendor_id', type=str, required=True, help="The device's vendor id in hex format")

        # TODO: provide the options for sign algorithm
        self.parser.add_argument('-sa', '--sign_algorithm',
                                 type=str, required=True, choices=["eddsa"], help="Choose which digital sign algorithm you want to use")
        self.parser.add_argument('-sd', '--start_date', type=str, default=datetime.now().strftime('%d-%m-%Y'),
                                 help="The starting date of file validation in dd-mm-yy format")
        self.parser.add_argument(
            '-ed', '--expire_date', type=str, help="The expiration date of file validation in dd-mm-yy format")

        # parse arguments
        arguments = self.parser.parse_args()

        self.CheckArguments(arguments)
        return

    # FIXME: CheckArguments
    def CheckArguments(self, arguments) -> None:

        try:

            # If an expiry date is not provided, then set it
            # to expire 10 days after the start date.
            if (arguments.expire_date == None):
                arguments.expire_date = (datetime.strptime(
                    arguments.start_date, '%d-%m-%Y') + timedelta(days=10)).strftime('%d-%m-%Y')

            # start date
            self.start_date = datetime.strptime(
                arguments.start_date, '%d-%m-%Y').strftime('%d-%m-%Y')

            # expire date
            self.expire_date = datetime.strptime(
                arguments.expire_date, '%d-%m-%Y').strftime('%d-%m-%Y')

            # if start date is older than expire date then throw error
            if (datetime.strptime(self.start_date, '%d-%m-%Y') > datetime.strptime(self.expire_date, '%d-%m-%Y')):
                ERROR("Start date > Expire date")

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

        except ValueError as ex:
            ERROR(ex)

        assert (self.file != None and
                self.manifest_id != None and
                self.vendor_id != None and
                self.product_id != None and
                self.file != None and
                self.start_date != None and
                self.expire_date != None and
                self.hash_type != None)
        return

    def CreateJSON(self) -> str:
        json_file = json.dumps(
            {"manifest_id": self.manifest_id, "vendor_id": self.vendor_id, "product_id": self.product_id, "start_date": self.start_date, "expire_date": self.expire_date})

        return json_file

    def __str__(self) -> str:
        return f"Argument object: manifest id={self.manifest_id} , vendor id={self.vendor_id} , product id={self.product_id} , start_date={self.start_date} , expire_date={self.expire_date} , hash type={self.hash_type} "
