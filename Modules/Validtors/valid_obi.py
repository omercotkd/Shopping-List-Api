def valid_object_id(oid):
    '''
    checks if a given input is a valid id of an
    object id
    '''
    if isinstance(oid, bytes):
        if len(oid) == 12:
            return True
        return False
    elif isinstance(oid, str):
        if len(oid) == 24:
            try:
                bytes.fromhex(oid)
            except (TypeError, ValueError):
                return False
            else:
                return True
    return False