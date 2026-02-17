stock_list = stock_list = [
    {
        'product': 'Apple',
        'amount': 50,
        'price': 0.50
    },
    {
        'product': 'Banana',
        'amount': 30,
        'price': 0.30
    },
    {
        'product': 'Orange',
        'amount': 40,
        'price': 0.40
    },
    {
        'product': 'Milk (1L)',
        'amount': 25,
        'price': 1.20
    },
    {
        'product': 'Bread',
        'amount': 15,
        'price': 1.50
    },
    {
        'product': 'Whiskey',
        'amount': 0,
        'price': 3.9
    }
]
total_value = 0
for item in stock_list:
    if item['amount'] != 0:
        item_value_total = item['amount'] * item['price']
        print(f"The total value of {item['product']} is: {item_value_total}")
        total_value += item_value_total
    else:
        print(f"{item['product']}, is out of stock")
print(f"The total value of all stock is: {total_value}")
    
