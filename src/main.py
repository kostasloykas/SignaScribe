import sys
from Arguments import *


def main():

    # Take Parameters and check the validity
    arg = Arguments()
    arg.ParseArguments()

    # TODO: create json object and parse the arguments
    json_file = arg.CreateJSON()
    DEBUG("JSON file: ", json_file)

    # TODO: take the firmware and save informations in json file

    # TODO: create and save the json file


if __name__ == "__main__":
    main()
