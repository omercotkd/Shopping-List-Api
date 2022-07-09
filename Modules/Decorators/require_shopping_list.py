from functools import wraps
import inspect
from Modules.DB_Collections.shopping_lists import Shoppinglists
from Modules.Validtors.valid_obi import valid_object_id
from Modules.Aggregitons.add_fields import _id_to_string
from Modules.Aggregitons.unset import unset_fields
from flask import jsonify, request

def require_shopping_list(func):
    @wraps(func)
    def inner(*args, **kwargs):

        params_ = request.args

        list_id = params_.get("list_id", "62c980c8248273db37f14e98")

        if not valid_object_id(list_id):
            return jsonify({"error": "list id"}), 400
        
        func_args = inspect.getfullargspec(func).args

        if "shopping_list" in func_args:

            shopping_list = Shoppinglists.objects(id=list_id)

            shopping_list = list(shopping_list)

            if not shopping_list:
                return jsonify({"error": "list id"}), 404

            shopping_list = shopping_list[0]

            kwargs["shopping_list"] = shopping_list

        if "shopping_list_dict" in func_args:

            shopping_list = Shoppinglists.objects(id=list_id).aggregate(
                [
                    _id_to_string(),
                    unset_fields(["_id"])

                ]
            )

            shopping_list = list(shopping_list)

            if not shopping_list:
                return jsonify({"error": "list id"}), 404

            shopping_list = shopping_list[0]

            kwargs["shopping_list_dict"] = shopping_list


        return func(*args, **kwargs)

    return inner