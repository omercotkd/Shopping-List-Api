def unset_fields(fields: list) -> dict:
    
    aggregtion = {
        "$unset": fields
    }
    
    return aggregtion
