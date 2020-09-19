insert_price = input('insert: ')
product_price = input('product: ')
change = int(insert_price) - int(product_price)

coins = [5000, 1000, 500, 100, 50, 10, 5, 1]

for coin in coins:
    r = change // coin
    change %= coin
    print(f"{coin}: {r}")

