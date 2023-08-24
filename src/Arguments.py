import argparse
from datetime import datetime


class Arguments:

    file = None
    manifest_id = None
    vendor_id = None
    product_id = None
    file = None
    start_date = None
    expire_date = None

    def __init__(self) -> None:

        pass

    def ParseArguments(self) -> None:

        self.parser = argparse.ArgumentParser(prog='SignaScribe')

        # define manifest fields
        # self.parser.add_argument('-mi', '--manifest_id',
        #                          type=int, required=True, help="Manifest ID")
        # self.parser.add_argument('-f', '--file', type=argparse.FileType("rw"), required=True,
        #                          help="The file that will be signed")
        # self.parser.add_argument(
        #     '-pi', '--product_id', type=int, required=True)
        # self.parser.add_argument('-vi', '--vendor_id', type=int, required=True)
        # self.parser.add_argument('-sa', '--sign_algorithm',
        #                          type=int, required=True, help="")
        self.parser.add_argument('-sd', '--start_date', type=str, default=datetime.now().strftime('%d-%m-%Y'),
                                 help="The starting date of image validation in dd-mm-yy format")
        self.parser.add_argument(
            '-ed', '--expire_date', type=str, help="The expiration date of image validation in dd-mm-yy format")

        # parse arguments
        arguments = self.parser.parse_args()

        self.CheckArguments(arguments)
        pass

    # FIXME: check the validity of arguments

    def CheckArguments(self, arguments):

        start_date = arguments.start_date

        print(arguments.start_date)

        try:
            print(datetime.strptime(arguments.start_date, '%d-%m-%Y'))
            pass
        except:
            pass

        assert (self.file != None and
                self.manifest_id != None and
                self.vendor_id != None and
                self.product_id != None and
                self.file != None and
                self.start_date != None and
                self.expire_date != None)
        pass

    def __str__(self) -> str:
        return f"Argument object: start_date={self.start_date}, expire_date={self.expire_date}"
