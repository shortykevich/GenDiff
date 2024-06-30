def mkdiff(key, value):
    return {
        "key": key,
        "value": value
    }


def mkvalues(file1_val, file2_val):
    return {
        "init val": file1_val,
        "new val": file2_val
    }


def get_diff_key(diff):
    return diff['key']


def get_diff_value(diff):
    return diff['value']


def get_diff_init_value(diff):
    return diff['value']['init val']


def get_diff_new_value(diff):
    return diff['value']['new val']
