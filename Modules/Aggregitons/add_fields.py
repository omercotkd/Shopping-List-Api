def _id_to_string() -> dict:

    aggregiton = {
        "$addFields": {
            "id": {"$toString": "$_id"}
        }
    }

    return aggregiton