#!/usr/bin/env python3
from gendiff.core import generate_diff
from gendiff.parser import get_arguments


def main():
    args = get_arguments()

    first_file = args.first_file
    second_file = args.second_file

    print(generate_diff(first_file, second_file))


if __name__ == "__main__":
    main()
