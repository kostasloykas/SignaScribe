import sys
from Arguments import *


def main(parameters):

    # Take Parameters and check the validity
    arg = Arguments()
    arg.ParseArguments()
    print(arg.__str__())


if __name__ == "__main__":
    main(sys.argv[1:])
