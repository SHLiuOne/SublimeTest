orders = [
    {'customer': 'Alice', 'amount': 120},
    {'customer': 'Bob', 'amount': 80},
    {'customer': 'Alice', 'amount': 30}
]

def calculate_total_spent(orders: list) -> dict:
    totals = {}
    for order in orders:
        customer = order['customer']
        amount = order['amount']
        if customer in totals:
            totals[customer] += amount
        else:
            totals[customer] = amount
    return totals

def find_top_customer(totals: dict) -> str:
    top_customer = None
    maximum = -1
    for customer in totals:
        if totals[customer] > maximum:
            maximum = totals[customer]
            top_customer = customer
    return top_customer


print(find_top_customer(calculate_total_spent(orders)))
