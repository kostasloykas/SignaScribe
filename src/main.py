from Arguments import *
from Firmware import *
from Certificate import *
from JSON import *


def main():

    # Take Parameters and check the validity
    arg = Arguments()
    arg.ParseArguments()

    # Load owner's certificate
    cert = Certificate(arg)
    # DEBUG(cert.certificate.subject.get_attributes_for_oid(
    #     NameOID.COMMON_NAME)[0]._value)

    # parse the firmware
    firmware = Firmware(arg)

    # TODO: make a signature file and write inside the signature

    # TODO: create and save the json file
    json_file = JSON(arg, firmware)
    json_file.SaveFile()

    # TODO: create zip file

    DEBUG("JSON file: ", json_file)


if __name__ == "__main__":
    main()
