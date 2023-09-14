from Arguments import *
from Firmware import *
from Certificate_Chain import Certificate_Chain
from JSON import *
from Zip import *
from Signature import *
from Saver import Saver
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.asymmetric.ed448 import Ed448PrivateKey


def PrivateKey(sign_algorithm) -> Ed25519PrivateKey | Ed448PrivateKey:
    private_key = None

    keys = {"eddsa25519":  Ed25519PrivateKey.generate(),
            "eddsa448": Ed448PrivateKey.generate()}
    private_key = keys.get(sign_algorithm)

    assert private_key
    return private_key


def main():

    # Take Parameters and check the validity
    arg = Arguments()
    arg.ParseArguments()
    print("Arguments Parsed Successfully")

    # Load owner's certificate and
    # validate the certificate chain
    certificate_chain = Certificate_Chain(arg)
    print("Certificate Chain Validation Passed")

    # load firmware
    firmware = Firmware(arg)
    print("Firmware Loaded Successfully")

    # TODO: Take private key (depends on sign algorithm)
    private_key = PrivateKey(arg.sign_algorithm)
    print("Private Key Generated Successfully")

    # create json file
    json_file = JSON(
        arg, firmware, certificate_chain.owner_certificate, private_key.public_key())
    print("JSON Configured")
    DEBUG(json_file)

    # TODO: make a signature file (needs json , firmware , certificate chain)
    signature = Signature(arg.sign_algorithm, arg.hash_algorithm, private_key,
                          firmware, json_file, certificate_chain)
    # print("Signature Created")
    return

    return

    # save all files to the predefined folder
    saver = Saver(firmware, json_file, certificate_chain, signature)

    # TODO: create zip file and insert the above files
    # zip = Zip(firmware, signature, certificate, json_file)
    # zip.SaveFile()


if __name__ == "__main__":
    main()
