#!/usr/bin/env python3
from gendiff import (
    generate_diff,
    open_file,
    get_arguments
)


def main():
    args = get_arguments()

    first_file = open_file(args.first_file)
    second_file = open_file(args.second_file)

    print(generate_diff(first_file, second_file))


if __name__ == "__main__":
    main()
