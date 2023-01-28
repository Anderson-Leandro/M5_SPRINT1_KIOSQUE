from menu.menu import products


def get_product_by_id(product_id):
   
    if(type(product_id) != int):
        raise TypeError("product id must be an int")

    for product in products:
        if(product["_id"] == product_id):
            return product
    return {}


def get_products_by_type(product_type):

    if(type(product_type) != str):
        raise TypeError("product type must be a str")

    result = products.copy()
    for product in products:
        if(product["type"] != product_type):
            result.remove(product)
    
    return result


def add_product(menu: list, **kwargs):
    menu.sort(key= lambda prod: prod["_id"])

    new_id = (menu[-1]["_id"] + 1) if len(menu) > 0 else 1

    new_prod = kwargs.copy()
    new_prod["_id"] = new_id

    menu.append(new_prod)

    return new_prod


def add_product_extra(menu: list, *args, **kwargs):

    required_keys = set(args)
    prod_keys = set(kwargs.keys())

    diference = prod_keys.difference(required_keys)

    for key in diference:
        del kwargs[key]
   
    for keys in args:
        if not kwargs.get(keys):
            raise KeyError(f"field {keys} is required")

    menu.sort(key= lambda prod: prod["_id"])

    new_id = (menu[-1]["_id"] + 1) if len(menu) > 0 else 1

    kwargs["_id"] = new_id

    menu.append(kwargs)

    return kwargs



def menu_report():
    product_count = len(products)
    average_price = round(sum([prod["price"] for prod in products]) / product_count, 2)
    
    prod_types = [prod["type"] for prod in products]
    set_types = set(prod_types)

    common_type = {"count": 0, "type": ""}    

    for types in set_types:
        count = prod_types.count(types)
        if count > common_type["count"]:
            common_type["count"] = count
            common_type["type"] = types
    
    return f"Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {common_type['type']}"
