from functools import wraps
from flask import jsonify, request

def check_content_type(content_type: str):

    def real_decorator(func):

        @wraps(func)

        def wrapper(*args, **kwargs):

            if not request.headers.get("Content-Type") == content_type:
                return jsonify({"error": f"Content-Type most be {content_type}"}),400
                    
            return func(*args, **kwargs)

        return wrapper
        
    return real_decorator