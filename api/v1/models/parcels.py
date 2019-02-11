"""parcels.py"""

from flask import jsonify


class Parcels:
    """class to create parcels"""

    parcels = []

    def __init__(self, parcel_id, parcel_name, user_id, quantity, price, status="enroute"):
        """ class that describes a parcel"""
        # self.parcel_id = uuid.uuid4()
        self.parcel_id = parcel_id
        self.parcel_name = parcel_name
        self.user_id = user_id
        self.quantity = quantity
        self.price = price
        self.status = status

    def to_dict(self):
        """returns dictionary format"""
        parcel_dict = {
            "parcel_id": self.parcel_id,
            "parcel_name": self.parcel_name,
            "user_id": self.user_id,
            "quantity": self.quantity,
            "price": self.price,
            "status": self.status
        }
        return parcel_dict

    def return_parcels(self):
        """method to return all parcels"""
        if len(self.parcels) == 0:
            return jsonify({"message": "No parcels ordered yet"}), 200
        return jsonify({
            "message": "Parcels retrieved successfully",
            "parcels": self.parcels
            }), 200

    def add_parcels(self):
        """add parcel"""
        self.parcels.append(self.to_dict())
        return jsonify({"message": "Parcel added successfully"}), 201

    def return_one_parcel(self, parcel_id):
        """return a single parcel"""
        if len(self.parcels) == 0:
            return jsonify({"message": "No parcels ordered yet"}), 200
        for parcel in self.parcels:
            if parcel["parcel_id"] == parcel_id:
                return jsonify({"message": "Parcel retrieved successfully", "parcel": parcel}), 200
        return jsonify({"message": "Parcel not found"}), 404

    def cancelled_parcel(self, parcel_id):
        """cancel parcel update"""
        for parcel in self.parcels:
            if parcel["parcel_id"] == parcel_id:
                self.status = "cancelled"
                return jsonify({
                    "message": "Parcel delivery cancelled",
                    "parcel": {
                        "parcel_id": parcel["parcel_id"],
                        "parcel_name": parcel["parcel_name"],
                        "user_id": parcel["user_id"],
                        "price": parcel["price"],
                        "quantity": parcel["quantity"],
                        "status": self.status
                    }
                }), 200
        return jsonify({"message": "Parcel not found"}), 404
