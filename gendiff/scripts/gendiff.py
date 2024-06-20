#!/usr/bin/env python3
import json


def open_file(file_path: str) -> tuple:
    return json.load(open(file_path))


def generate_diff(file1_path: str,
                  file2_path: str) -> str:
    file1, file2 = open_file(file1_path), open_file(file2_path)
    files_union = file1 | file2
    sorted_files_union = dict(sorted(files_union.items()))

    diffs = []
    for key, val in sorted_files_union.items():
        is_key_in_file1 = key in file1
        is_key_in_file2 = key in file2
        val_in_file1 = file1.get(key)

        if is_key_in_file2 and not is_key_in_file1:
            diffs.append(f"+ {key}: {val}")
        elif is_key_in_file1 and not is_key_in_file2:
            diffs.append(f"- {key}: {val}")
        elif is_key_in_file1 and val_in_file1 == val:
            diffs.append(f"  {key}: {val}")
        elif is_key_in_file1 and val_in_file1 != val:
            diffs.append(f"- {key}: {file1[key]}\n"
                         f"+ {key}: {val}")

    return '{\n' + '\n'.join(diffs) + '\n}'
