def is_none(obj):
    if obj is None:
        return True
    return False


def is_empty(string):
    if not string:
        return True
    return False


def is_valid(obj):
    if is_none(obj) or is_empty(obj):
        return False
    return True
