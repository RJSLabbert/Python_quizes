orders = [
    {'order_id': 'A1', 'timestamp': 1678886400, 'items': ['Laptop', 'Mouse', 'Keyboard']},
    {'order_id': 'B2', 'timestamp': 1678890000, 'items': ['Laptop', 'External Hard Drive']},
    {'order_id': 'C3', 'timestamp': 1678893600, 'items': ['Monitor', 'Keyboard']},
    {'order_id': 'D4', 'timestamp': 1678897200, 'items': ['Laptop', 'Mouse', 'Laptop']}
]

def process_priority_orders(orders, high_demand_item):
    priority_list = []
    for order in orders:
        if high_demand_item in order['items']:
            new_order = order.copy()
            new_order['items'] = list(set(order['items']))
            priority_list.append(new_order)
    return sorted(priority_list, key=lambda x: x['timestamp'], reverse=True)

print(process_priority_orders(orders, 'Mouse'))    
