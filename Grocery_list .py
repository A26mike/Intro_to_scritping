#python 3.8.2

grocery_item = {}
grocery_history = []
stop = 'c'  # set to continue
grand_total = 0


def format_price(amount):
    """format_price [formated to a price to two decmial places]

    Args:
        amount (Float): A price for conversion 

    Returns:
        [float]: [formated to  two decmial places ]
    """
    return str(format(amount, '.2f'))


while stop.lower() != 'q':
    # Get input from user (item , quanity, cost)
    item_name = input("Item name:\n")
    # Accept input of the quantity of the grocery item purchased.
    quantity = input("Quantity purchased:\n")
    # Accept input of the cost of the grocery item input (this is a per-item cost).
    cost = input("Price per item:\n")
    # dictionary entry which contains the name, number and price entered by the user.
    grocery_item = {'name': item_name,
                    'number': int(quantity),
                    'price': float(cost)}
    grocery_history.append(grocery_item)
    stop = input(
        "Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n")

# loop through all items in grocery list and print out in format
for item in grocery_history:
    item_total = item['number'] * item['price']
    grand_total += item_total
    # varibles to help with formating with printing
    item_quanity = (str(item['number']))
    item_name = str(item['name'])
    item_price = format_price(item['price'])

    print(
        f"""{item_quanity} {item_name} @ ${item_price} ea ${format_price(item_total)}""")
    item_total = 0  # reset varible to 0 for each item

print('Grand total: $' + format_price(grand_total))

# other war using string concatination
#print(str(item['number']) , str(item['name']) , "@ $" + format_price(item['price']), 'ea', '$'+ format(item_total))
