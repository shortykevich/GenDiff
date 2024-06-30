from gendiff.constants import (
    get_added,
    get_removed
)
from gendiff.core.diff import (
    get_diff_key,
    get_diff_value,
    get_diff_init_value,
    get_diff_new_value
)


def format_val(value, depth, indent="    "):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    elif not isinstance(value, dict):
        return value

    strs = ["{"]
    for key, val in value.items():
        if isinstance(val, dict):
            strs.append(f"{indent * depth}{key}: {format_val(val, depth+1)}")
        else:
            strs.append(f"{indent * depth}{key}: {val}")
    strs.append(f"{indent * (depth-1)}" + "}")

    return '\n'.join(strs)


def stylish_format(diffs, depth=1, sep="    "):
    indent_temp = sep * depth
    strs = ["{"]
    for diff in diffs:
        key = get_diff_key(diff)
        val = get_diff_value(diff)

        if isinstance(val, list):
            strs.append(f"{indent_temp}{key}: {stylish_format(val, depth+1)}")
            continue

        init_val = get_diff_init_value(diff)
        new_val = get_diff_new_value(diff)
        added = get_added()
        removed = get_removed()

        if init_val == get_added():  # Added
            indent = indent_temp[:-2] + added
            strs.append(f"{indent}{key}: {format_val(new_val, depth+1)}")
        elif new_val == get_removed():  # Removed
            indent = indent_temp[:-2] + removed
            strs.append(f"{indent}{key}: {format_val(init_val, depth+1)}")
        elif init_val == new_val:  # Unchanched
            indent = sep * depth
            strs.append(f"{indent}{key}: {format_val(init_val, depth+1)}")
        else:  # Updated
            init_indent = indent_temp[:-2] + removed
            upd_indent = indent_temp[:-2] + added
            strs.append(f"{init_indent}{key}: {format_val(init_val, depth+1)}")
            strs.append(f"{upd_indent}{key}: {format_val(new_val, depth+1)}")

    strs.append(f"{sep * (depth-1)}""}")
    return '\n'.join(strs)
