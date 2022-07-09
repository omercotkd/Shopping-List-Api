from flask import Blueprint, jsonify, request
from Modules.Decorators.require_shopping_list import require_shopping_list
from Modules.Decorators.content_type import check_content_type
from Modules.DB_Collections.shopping_lists import shoppinglists, ShoppingItem
from Modules.Validtors.instance import check_value_and_instance


manage_lists_routes = Blueprint("manage_lists_routes", __name__, url_prefix="/api/shoping-list")


@manage_lists_routes.route("", methods=["POST"])
@check_content_type("application/json")
def create_new_shopping_list():

    json_ = request.json

    name = json_.get("name")

    if not check_value_and_instance(name, str):
        return jsonify({"error": "name"}), 400

    new_list = shoppinglists(
        name = name
    )

    new_list.save()

    return jsonify({"massage": "sucsess"}), 201
    

@manage_lists_routes.route("", methods=["GET"])
@require_shopping_list
def get_shopping_list(shopping_list_dict: dict):

    return jsonify({"list": shopping_list_dict})


@manage_lists_routes.route("/item", methods=["POST"])
@check_content_type("application/json")
@require_shopping_list
def add_item_to_list(shopping_list: shoppinglists):

    json_ = request.json

    name = json_.get("name")
    amount = json_.get("amount")
    unit = json_.get("unit")

    if not check_value_and_instance(name, str):
        return jsonify({"error": "name"}), 400
    elif not check_value_and_instance(amount, int):
        return jsonify({"error": "amount"}), 400
    elif not check_value_and_instance(unit, str):
        return jsonify({"error": "unit"}), 400

    if not amount > 0:
        return jsonify({"error": "amount need to be positive"}), 400

    new_item = ShoppingItem(
        name = name,
        amount = amount,
        unit = unit
    )

    shopping_list.items.append(new_item)

    shopping_list.save()

    return jsonify({"massage":"succsess"}), 201


@manage_lists_routes.route("/item", methods=["DELETE"])
@require_shopping_list
def delete_item_from_list(shopping_list: shoppinglists):

    item_id = request.args.get("item_id")

    if not item_id:
        return jsonify({"error": "item_id"}), 404

    shoppinglists.objects(id=shopping_list.id).update()

    return ""

