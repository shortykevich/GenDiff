def universal_formater(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    elif not isinstance(value, dict):
        return value
    else:
        return None
