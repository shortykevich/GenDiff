from gendiff.parser.parse import open_file
from gendiff.constants import NOT_FOUND
from gendiff.core.formaters import (
    stylish,
    plain,
    json
)
from gendiff.core.diff import (
    mkdiff,
    mkvalues
)


def make_internal_diff(file1, file2):
    merged_files = file1 | file2
    merged_files = dict(sorted(merged_files.items()))

    diffs = []
    for key in merged_files.keys():
        file1_val = file1.get(key, NOT_FOUND)
        file2_val = file2.get(key, NOT_FOUND)

        if isinstance(file1_val, dict) and isinstance(file2_val, dict):
            internal_diff = make_internal_diff(file1_val, file2_val)
            diffs.append(
                mkdiff(key, internal_diff)
            )
        else:
            diffs.append(
                mkdiff(key, mkvalues(file1_val, file2_val))
            )
    return diffs


def generate_diff(file1_path, file2_path, formater_name='stylish'):
    file1, file2 = open_file(file1_path), open_file(file2_path)
    diff = make_internal_diff(file1, file2)

    match formater_name:
        case 'plain':
            return plain(diff)
        case 'json':
            return json(diff)
        case _:
            return stylish(diff)
