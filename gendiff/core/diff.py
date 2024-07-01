def mkdiff(key, value):
    return {
        'key': key,
        'values': value
    }


def mkvalues(file1_val, file2_val):
    return {
        'init val': file1_val,
        'new val': file2_val
    }


def get_diff_key(diff):
    return diff['key']


def get_diff_values(diff):
    return diff['values']


def get_diff_init_value(value):
    return value['init val']


def get_diff_new_value(value):
    return value['new val']
