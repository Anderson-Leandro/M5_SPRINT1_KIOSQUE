from menu.menu import products


def calculate_tab(prod_table):
    subtotal = 0

    for prod in prod_table:
        price = [product["price"] for product in products if product["_id"] == prod["_id"]]
                
        subtotal += price[0] * prod["amount"]

    return {"subtotal": f"${round(subtotal, 2)}"}