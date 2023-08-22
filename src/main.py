import sys
import argparse


def main(parameters):

    # Parameters
    parser = argparse.ArgumentParser(prog='SignaScribe')
    parser.add_argument('-f', '--file', required=True)

    parser.parse_args()


if __name__ == "__main__":
    main(sys.argv[1:])
