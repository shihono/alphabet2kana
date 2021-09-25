import argparse

import alphabet2kana

from .alphabet2kana import a2k


def parse_args(test=None):
    parser = argparse.ArgumentParser(
        prog="a2k",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Convert English alphabet to Katakana",
    )
    parser.add_argument(
        "text", metavar="text", type=str, help="Half-width English alphabet string"
    )
    parser.add_argument(
        "-d", "--delimiter", type=str, metavar="char", help="Katakana delimiter"
    )
    parser.add_argument(
        "-n", "--numeral", action="store_true", help="Convert Arabic numerals"
    )
    parser.add_argument(
        "-V", "--version", action="version", version=alphabet2kana.__version__
    )
    if test:
        return parser.parse_args(test)
    else:
        return parser.parse_args()


def main():
    args = parse_args()
    res = a2k(args.text, delimiter=args.delimiter, numeral=args.numeral)
    print(res)


if __name__ == "__main__":
    main()
