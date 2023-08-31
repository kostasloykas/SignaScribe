from Arguments import *
from Firmware import *
from Certificate import *
from JSON import *
from Zip import *
from Signature import *


def main():

    # Take Parameters and check the validity
    arg = Arguments()
    arg.ParseArguments()

    # Load owner's certificate
    certificate = Certificate(arg)

    return

    # parse the firmware
    firmware = Firmware(arg)

    # create json file
    json_file = JSON(arg, firmware)
    json_file.SaveFile()

    # TODO: make a signature file and write the signature
    # signature = Signature()
    # signature.SaveFile()

    # TODO: create zip file and save inside firmware,
    # # json file , certificate and signature
    # zip = Zip(firmware, signature, certificate, json_file)
    # zip.SaveFile()


if __name__ == "__main__":
    main()
