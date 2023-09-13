from Arguments import *
from Firmware import *
from Certificate_Chain import Certificate_Chain
from JSON import *
from Zip import *
from Signature import *
from Saver import Saver


def main():

    # Take Parameters and check the validity
    arg = Arguments()
    arg.ParseArguments()
    print("Argument Parsed Successfuly")

    # Load owner's certificate and
    # validate the certificate chain
    certificate_chain = Certificate_Chain(arg)
    print("Certificate Chain Validation Passed")

    # parse the firmware
    firmware = Firmware(arg)

    # create json file
    json_file = JSON(arg, firmware)

    return
    # TODO: make a signature file and write the signature (needs json , firmware , certificate chain)
    signature = Signature()

    # save all files to the predefined folder
    saver = Saver(firmware, json_file, certificate_chain, signature)
    saver.SaveAllFiles()

    # TODO: create zip file and insert the above files
    # zip = Zip(firmware, signature, certificate, json_file)
    # zip.SaveFile()


if __name__ == "__main__":
    main()
