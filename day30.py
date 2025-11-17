import pandas as pd
data = {
    'date': ['2023-07-01', '2023-07-01', '2023-07-02'],
    'dish': ['Pasta', 'Salad', 'Burger'],
    'quantity': [2, 1, 3],
    'order_type': ['dine-in', 'takeout', 'dine-in']
}
orders = pd.DataFrame(data)

high_orders = orders[orders['quantity'] >= 2]
takeout_orders = orders[orders['order_type'] == 'takeout']

data1 = {
    "workout": ["Upper", "Lower", "Legs", "Swimming"],
    "type": ["Weights", "Weights", "Weights", "Cardio"],
    "time": [60, 60, 60, 30], 

}

exercise_data = pd.DataFrame(data1)

morethan_45 = exercise_data[exercise_data["time"] >= 45]


