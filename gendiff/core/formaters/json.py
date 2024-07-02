from json import dumps


def json(tree):
    return dumps(tree, indent=4)
