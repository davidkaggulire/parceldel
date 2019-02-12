"""views.py"""

from flask import jsonify, request
from api.v1 import app
from api.v1.models.parcels import Parcels

parcel = Parcels(1, "juice", 1, 40, 1000)


@app.route('/')
def home():
    """returns home welcome message"""
    return jsonify({"message": 'parceldel connecting you'})


@app.route('/parcels', methods=['POST'])
def post_parcels():
    """Store parcel in db structure"""

    try:
        form_data = request.get_json(force=True)
        parcel_id = len(Parcels.parcels) + 1
        parcel_name = form_data['parcel_name']
        user_id = form_data['user_id']
        quantity = form_data['quantity']
        price = form_data['price']

        parcel = Parcels(parcel_id, parcel_name, user_id, quantity, price)
        return parcel.add_parcels()
    except KeyError:
        return jsonify({"message": "Input field missing"}), 401


@app.route('/parcels')
def get_all_parcels():
    """returns all parcels"""
    return parcel.return_parcels()


@app.route('/parcels/<int:parcel_id>')
def get_single_parcel(parcel_id):
    """return single parcel"""
    return parcel.return_one_parcel(parcel_id)


@app.route('/parcels/<int:parcel_id>/cancel', methods=['PUT'])
def cancel_parcel(parcel_id):
    """route to cancel parcel"""
    return parcel.cancelled_parcel(parcel_id)


@app.route('/users/<int:user_id>/parcels', methods=['GET'])
def fetch_parcel_by_user(user_id):
    order_list = []
    for order in Parcels.parcels:
        if order["user_id"] == user_id:
            order_list.append(order)

    if len(order_list) > 0:
        return jsonify({
            "message": "Parcels ordered by user_id {}".format(user_id),
            "parcel": order_list
        }), 200
    else:
        return jsonify({"message": "User not found"}), 404
