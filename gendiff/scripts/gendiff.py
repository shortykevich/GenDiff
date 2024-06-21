import json


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'None'
    else:
        return str(value)


def open_file(file_path: str) -> dict:
    return json.load(open(file_path))


def generate_diff(file1: dict,
                  file2: dict) -> str:
    sorted_files_union = dict(sorted(
        (file1 | file2).items()
    ))

    diffs = []
    for key, val in sorted_files_union.items():
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
            diffs.append(f"- {key}: {format_value(file1[key])}\n"
                         f"+ {key}: {formated_val}")

    return '{\n' + '\n'.join(diffs) + '\n}'


print(json.load(open("JSON_files/file1.json")))
print()
print(json.load(open("JSON_files/file2.json")))
