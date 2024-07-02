#!/usr/bin/env python3
from gendiff.core import generate_diff
from gendiff.parser import get_arguments


def main():
    args = get_arguments()

    first_file = args.file1
    second_file = args.file2
    formater = args.format

    print(generate_diff(first_file, second_file, formater))


if __name__ == "__main__":
    main()
