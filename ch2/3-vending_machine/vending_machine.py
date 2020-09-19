import sys

insert_price = input('insert: ')
if not insert_price.isdecimal():
    print('Please input an integer.')
    sys.exit()

product_price = input('product: ')
if not product_price.isdecimal():
    print('Please input an integer.')
    sys.exit()

change = int(insert_price) - int(product_price)
if change < 0:
    print('Insufficient charges')
    sys.exit()

coins = [5000, 1000, 500, 100, 50, 10, 5, 1]

for coin in coins:
    r = change // coin
    change %= coin
    print(f"{coin}: {r}")

