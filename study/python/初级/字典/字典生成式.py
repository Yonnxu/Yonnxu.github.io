items = ['Fruits', 'Books', 'Others']
prices = [96, 78, 85]
d = {items.upper(): prices for items, prices in zip(items, prices)}
print(d)

d = {items: prices for prices, items in zip(prices, items)}
print(d)

