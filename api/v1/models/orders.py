"""orders.py"""


class Orders:
    def __init__(self, order_id, parcel_id, user_id, order_count):
        self.order_id = order_id
        self.parcel_id = parcel_id
        self.user_id = user_id
        self.order_count = order_count

    def to_dict(self):
        order_dict = {
            "order_id": self.order_id,
            "parcel_id": self.parcel_id,
            "user_id": self.user_id,
            "order_count": self.order_count
        }

        return order_dict
