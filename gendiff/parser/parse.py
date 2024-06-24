import json
import yaml
import argparse


def get_arguments():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    return parser.parse_args()


def open_file(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        return (
            json.load(file)
            if file_path.endswith('.json')
            else yaml.safe_load(file)
        )


def merge_and_sort_files(file1: dict,
                         file2: dict) -> dict:
    merged_files = file1 | file2
    sorted_merged_files = dict(sorted(merged_files.items()))
    return sorted_merged_files
