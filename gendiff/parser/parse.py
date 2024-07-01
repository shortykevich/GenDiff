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
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument(
        "-f", "--format",
        help="set format of output",
        default="stylish",
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    return parser.parse_args()
