import sys
from Arguments import *
from Certificate import *


def main():

    # Take Parameters and check the validity
    arg = Arguments()
    arg.ParseArguments()

    # Load owner's certificate
    cert = Certificate(arg.certificate)
    # DEBUG(cert.certificate.extensions)

    # TODO: create json object and parse the arguments
    json_file = arg.CreateJSON()
    DEBUG("JSON file: ", json_file)

    # TODO: take the firmware and save informations in json file

    # TODO: create and save the json file


if __name__ == "__main__":
    main()
