import sys
from Arguments import *


def main(parameters):

    # Take Parameters and check the validity
    arg = Arguments()
    arg.ParseArguments()


if __name__ == "__main__":
    main(sys.argv[1:])
