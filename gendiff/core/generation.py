from gendiff.parser.parse import open_file
from gendiff.constants import NOT_FOUND
from gendiff.core.formaters import stylish
from gendiff.core.diff import (
    mkdiff,
    mkvalues
)


def merge_and_sort_files(file1, file2):
    merged_files = file1 | file2
    return dict(sorted(merged_files.items()))


def generate_diff(file1_path, file2_path, formater=stylish):
    file1, file2 = open_file(file1_path), open_file(file2_path)

    def walk(dict1, dict2):
        merged_files = merge_and_sort_files(dict1, dict2)

        diffs = []
        for key in merged_files.keys():
            file1_val = dict1.get(key, NOT_FOUND)
            file2_val = dict2.get(key, NOT_FOUND)

            if isinstance(file1_val, dict) and isinstance(file2_val, dict):
                internal_diff = walk(file1_val, file2_val)
                diffs.append(
                    mkdiff(key, internal_diff)
                )
            else:
                diffs.append(
                    mkdiff(key, mkvalues(file1_val, file2_val))
                )
        return diffs

    return formater(walk(file1, file2))
