result = {}
with open("C:/Projects/SublimeTest/orders.txt") as orders:
    for line in orders:
        name, amount = line.strip().split(',')
        if name in result:
            result[name] += float(amount)
        else:
            result[name] = float(amount) 

print(result)
