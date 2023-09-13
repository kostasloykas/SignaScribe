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
    print("Arguments Parsed Successfully")

    # TODO: create private key and public (depends on sign algorithm)

    # Load owner's certificate and
    # validate the certificate chain
    certificate_chain = Certificate_Chain(arg)
    print("Certificate Chain Validation Passed")

    # load firmware
    firmware = Firmware(arg)
    print("Firmware Loaded Successfully")

    # create json file
    json_file = JSON(arg, firmware, certificate_chain.owner_certificate)
    print("JSON Configured")
    DEBUG(json_file)

    return

    # TODO: make a signature file (needs json , firmware , certificate chain)
    signature = Signature(arg.sign_algorithm, arg.hash_algorithm,
                          firmware, json_file, certificate_chain)
    print("Signature Created")

    return

    # save all files to the predefined folder
    saver = Saver(firmware, json_file, certificate_chain, signature)

    # TODO: create zip file and insert the above files
    # zip = Zip(firmware, signature, certificate, json_file)
    # zip.SaveFile()


if __name__ == "__main__":
    main()
