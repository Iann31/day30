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


print(orders.iloc[0][0])
