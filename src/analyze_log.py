import os
import csv
from typing import Counter


def path_validator(path):
    if not path.endswith('.csv') or not os.path.exists(path):
        raise FileNotFoundError(f"No such file or directory: '{path}'")


def reader(path):
    with open(path) as file:
        data = csv.reader(file, delimiter=',')
        return [order for order in data]


def dish_most_requested(customer_name, data):
    orders = [
        order[1] for order in data
        if customer_name == order[0]
    ]

    return Counter(orders).most_common(1)[0][0]


def dish_counter(customer_name, data):
    orders = [
        order[1] for order in data
        if customer_name == order[0] and order[1] == 'hamburguer'
    ]

    return len(orders)


def dish_never_ordered(customer_name, data):
    menu = {dish[1] for dish in data}

    orders = {
        order[1] for order in data
        if customer_name == order[0]
    }

    return (menu - orders)


def days_never_attended(customer_name, data):
    days_week = {day[2] for day in data}

    day_attended = {
        day[2] for day in data
        if customer_name == day[0]
    }

    return (days_week - day_attended)


def data_saver(most_requested, quantity, never_ordered, never_attended):
    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(
            f'{most_requested}\n'
            f'{quantity}\n'
            f'{never_ordered}\n'
            f'{never_attended}\n'
        )


def analyze_log(path_to_file):
    path_validator(path_to_file)
    datalog = reader(path_to_file)

    most_requested = dish_most_requested('maria', datalog)
    quantity = dish_counter('arnaldo', datalog)
    never_ordered = dish_never_ordered('joao', datalog)
    never_attended = days_never_attended('joao', datalog)
    data_saver(most_requested, quantity, never_ordered, never_attended)
