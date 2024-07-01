from gendiff.constants import NOT_FOUND
from gendiff.core.diff import (
    get_diff_key,
    get_diff_values,
    get_diff_init_value,
    get_diff_new_value
)


def stylish_val(value, depth, indent="    "):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    elif not isinstance(value, dict):
        return value

    strs = ["{"]
    for key, val in value.items():
        if isinstance(val, dict):
            strs.append(f"{indent * depth}{key}: {stylish_val(val, depth+1)}")
        else:
            strs.append(f"{indent * depth}{key}: {val}")
    strs.append(f"{indent * (depth-1)}" + "}")

    return '\n'.join(strs)


def stylish(tree, depth=1, sep="    "):
    indent = sep * depth
    strs = ["{"]
    for diff in tree:
        key = get_diff_key(diff)
        val = get_diff_values(diff)

        if isinstance(val, list):
            strs.append(f"{indent}{key}: {stylish(val, depth + 1)}")
            continue

        init_val = get_diff_init_value(val)
        new_val = get_diff_new_value(val)
        added = indent[:-2] + '+ '
        removed = indent[:-2] + '- '

        if init_val is NOT_FOUND:  # Added
            strs.append(f"{added}{key}: {stylish_val(new_val, depth+1)}")
        elif new_val is NOT_FOUND:  # Removed
            strs.append(f"{removed}{key}: {stylish_val(init_val, depth+1)}")
        elif init_val == new_val:  # Unchanched
            strs.append(f"{indent}{key}: {stylish_val(init_val, depth+1)}")
        else:  # Updated
            strs.append(f"{removed}{key}: {stylish_val(init_val, depth+1)}")
            strs.append(f"{added}{key}: {stylish_val(new_val, depth+1)}")

    strs.append(f"{sep * (depth-1)}""}")
    return '\n'.join(strs)