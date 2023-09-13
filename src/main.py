from Arguments import *
from Firmware import *
from Certificate_Chain import Certificate_Chain
from JSON import *
from Zip import *
from Signature import *


def main():

    # Take Parameters and check the validity
    arg = Arguments()
    arg.ParseArguments()
    print("Argument Parsed")

    # Load owner's certificate and
    # validate the certificate chain
    certificate_chain = Certificate_Chain(arg)
    print("Certificate Chain Validation Passed")

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
