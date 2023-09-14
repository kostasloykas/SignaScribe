from Arguments import *
from Firmware import *
from Certificate_Chain import Certificate_Chain
from JSON import *
from Zip import *
from Signature import *
from Saver import Saver
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.asymmetric.ed448 import Ed448PrivateKey
from Signature import SUPPORTED_PRIVATE_KEYS, SUPPORTED_HASH_ALGORITHMS
from cryptography.hazmat.primitives.hashes import MD5, SHA256, SHAKE256


def PrivateKey(sign_algorithm) -> SUPPORTED_PRIVATE_KEYS:
    private_key = None

    keys = {"eddsa25519":  Ed25519PrivateKey.generate(),
            "eddsa448": Ed448PrivateKey.generate()}
    private_key = keys.get(sign_algorithm)

    assert private_key
    return private_key


# FIXME: Make it support md5 algorithm
def TakeHashAlgorithm(hash_algorithm) -> SUPPORTED_HASH_ALGORITHMS:
    hash = None

    hashes = {"sha256": SHA256(),
              "md5": MD5()}
    hash = hashes.get(hash_algorithm)

    assert hash
    return hash


def main():

    # Take Parameters and check the validity
    arg = Arguments()
    arg.ParseArguments()
    print("Arguments Parsed Successfully")

    # Load firmware
    firmware = Firmware(arg)
    print("Firmware Loaded Successfully")
    # Load owner's certificate and

    # validate the certificate chain
    certificate_chain = Certificate_Chain(arg)
    print("Certificate Chain Validation Passed")

    # Generate a private key according to sign algorithm
    private_key = PrivateKey(arg.sign_algorithm)
    print("Private Key Generated Successfully")

    # Create json file
    json_file = JSON(
        arg, firmware, certificate_chain.owner_certificate, private_key.public_key())
    print("JSON Configured")

    # Sign the files
    signature = Signature(arg.sign_algorithm, TakeHashAlgorithm(arg.hash_algorithm), private_key,
                          firmware, json_file, certificate_chain)
    print("Process of signing completed sucessfully")

    # save all files to the predefined folder
    saver = Saver(firmware, json_file, certificate_chain, signature)

    return

    # TODO: create zip file and insert the above files
    # zip = Zip(firmware, signature, certificate, json_file)
    # zip.SaveFile()


if __name__ == "__main__":
    main()
