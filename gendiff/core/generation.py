from gendiff.parser.parse import merge_and_sort_files
from gendiff.constants import (
    get_added,
    get_removed
)
from gendiff.core.diff import (
    mkdiff,
    mkvalues
)


def generate_diff(file1: dict,
                  file2: dict) -> list:
    merged_files = merge_and_sort_files(file1, file2)

    diffs = []
    for key in merged_files.keys():
        added = get_added()
        removed = get_removed()
        file1_val = file1.get(key, added)
        file2_val = file2.get(key, removed)

        if isinstance(file1_val, dict) and isinstance(file2_val, dict):
            internal_diff = generate_diff(file1_val, file2_val)
            diffs.append(
                mkdiff(key, internal_diff)
            )
        else:
            diffs.append(
                mkdiff(key, mkvalues(file1_val, file2_val))
            )

    return diffs
