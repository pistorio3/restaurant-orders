from typing import Counter


class TrackOrders:
    def __len__(self):
        return len(self.orders)

    def __init__(self):
        self.orders = []

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_costumer(self, customer):
        most_ordered_dish = [
            order[1] for order in self.orders
            if customer == order[0]
        ]

        return Counter(most_ordered_dish).most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, customer):
        pass

    def get_days_never_visited_per_costumer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
