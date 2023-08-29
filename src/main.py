from Arguments import *
from Certificate import *


def main():

    # Take Parameters and check the validity
    arg = Arguments()
    arg.ParseArguments()

    # Load owner's certificate
    cert = Certificate(arg)
    # DEBUG(
    #     cert.certificate.public_key().public_bytes(
    #         encoding=serialization.Encoding.PEM,
    #         format=serialization.PublicFormat.SubjectPublicKeyInfo
    #     ))
    # DEBUG(cert.certificate.subject.get_attributes_for_oid(
    #     NameOID.COMMON_NAME)[0]._value)

    # create from arguments a json file
    json_file = arg.CreateJSON()
    DEBUG("JSON file: ", json_file)

    # TODO: take the firmware and save informations in json file

    # TODO: create and save the json file

    # TODO: assign the signature in json file


if __name__ == "__main__":
    main()
