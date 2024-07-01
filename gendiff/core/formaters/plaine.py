from gendiff.constants import NOT_FOUND
from gendiff.core.diff import (
    get_diff_key,
    get_diff_values,
    get_diff_init_value,
    get_diff_new_value
)


def plain_val(value):
    return (
        "[complex value]" if isinstance(value, dict) else
        f"'{value}'" if isinstance(value, str) else
        str(value).lower() if isinstance(value, bool) else
        "null" if value is None else
        value
    )


def plain(tree, ancestors=''):
    strs = []
    for diff in tree:
        key = get_diff_key(diff)
        val = get_diff_values(diff)

        if isinstance(val, list):
            strs.append(plain(val, ancestors + key + '.'))
            continue

        temp = f"Property '{ancestors + key}' was "
        init_val = get_diff_init_value(val)
        new_val = get_diff_new_value(val)

        if init_val is NOT_FOUND:  # Added
            strs.append(
                temp + f"added with value: {plain_val(new_val)}"
            )
        elif new_val is NOT_FOUND:  # Removed
            strs.append(temp + "removed")
        elif init_val != new_val:  # Updated
            strs.append(
                temp + "updated. "
                f"From {plain_val(init_val)} to "
                f"{plain_val(new_val)}"
            )

    return '\n'.join(strs)