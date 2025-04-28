customers = ['Alice', 'Bob', 'Charlie']
orders = [120, 80, 200]

def find_orders(customers: list, orders: list) -> dict:
    return dict(zip(customers, orders))

print(find_orders(customers,orders))

def find_rich(order_list: dict) -> list:
    rich_list = []
    for customer in order_list:
        if order_list[customer] > 100:
            rich_list.append(customer)
    return rich_list

print(find_rich(find_orders(customers,orders)))
