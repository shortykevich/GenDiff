#!/usr/bin/env python3
from gendiff.core import (
    generate_diff,
    plain
)
from gendiff.parser import (
    open_file,
    get_arguments
)


def main():
    args = get_arguments()

    first_file = open_file(args.first_file)
    second_file = open_file(args.second_file)

    match args.format:
        case 'plain':
            print(generate_diff(first_file, second_file, plain))
        case _:
            print(generate_diff(first_file, second_file))


if __name__ == "__main__":
    main()
