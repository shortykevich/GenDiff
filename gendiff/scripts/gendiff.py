import json


def format_value(value):
    return str(value).lower() if isinstance(value, bool) else str(value)


def open_file(file_path: str) -> dict:
    return json.load(open(file_path))


def merge_and_sort_files(file1: dict,
                         file2: dict) -> dict:
    merged_files = file1 | file2
    sorted_merged_files = dict(sorted(merged_files.items()))
    return sorted_merged_files


def generate_diff(file1: dict,
                  file2: dict) -> str:
    merged_files = merge_and_sort_files(file1, file2)

    diffs = []
    for key, val in merged_files.items():
        is_key_in_file1 = key in file1
        is_key_in_file2 = key in file2
        val_in_file1 = file1.get(key)
        formated_val = format_value(val)

        if is_key_in_file2 and not is_key_in_file1:
            diffs.append(f"+ {key}: {formated_val}")
        elif is_key_in_file1 and not is_key_in_file2:
            diffs.append(f"- {key}: {formated_val}")
        elif is_key_in_file1 and val_in_file1 == val:
            diffs.append(f"  {key}: {formated_val}")
        elif is_key_in_file1 and val_in_file1 != val:
            file1_formatted_val = format_value(val_in_file1)
            diffs.append(f"- {key}: {file1_formatted_val}\n"
                         f"+ {key}: {formated_val}")

    return '{\n' + '\n'.join(diffs) + '\n}'
