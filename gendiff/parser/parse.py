import json
import yaml
import argparse


def open_file(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        return (
            json.load(file)
            if file_path.endswith('.json')
            else yaml.safe_load(file)
        )


def get_arguments():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        usage="%(prog)s [options] <filepath1> <filepath2>"
    )
    parser.add_argument(
        "-f", "--format",
        help="set format type of output [stylish, plain, json]"
             "(default: stylish)",
        metavar="[type]",
        choices=['stylish', 'plain', 'json'],
        default="stylish",
        required=False
    )
    parser.add_argument("file1", help="Path to first file")
    parser.add_argument("file2", help="Path to second file")
    return parser.parse_args()
