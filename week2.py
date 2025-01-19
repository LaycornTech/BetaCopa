def add_to_cart(item_name, item_price, color, size, *discount, **cart):
    cart = {}
    cart["item_name"] = item_name
    cart["item_price"] = item_price
    cart["discount"] = discount
    cart["color"] = color
    cart["size"]= size 
    return cart


def calculate_discount(current_cart):
    price_of_item = current_cart["item_price"]
    discount = current_cart["discount"]
    total_discounts = discount[0] * price_of_item
    net_cost = price_of_item - total_discounts

    return int(net_cost)

def check_For_duplicate(container, item_name):

    for item in range(len(container)):
        name = container[item]
        if (name["item_name"] == item_name):
            container.remove(name)
    return container

        
def user_response():
    polling_active = True
    container = []
    while (polling_active):
        item_name = input("Enter item name or done to finish: ")
        if (item_name == "done"):
            polling_active = False
            break
        item_price = int(input("Enter Price: "))
        discount = float(input("Enter discount if any: "))
        # print("===============Enter Item details e.g color = red =======================")
        color = input("Enter color: ")
        size = input("Enter size: ")

        current_cart = add_to_cart(item_name, item_price, color,size, discount)
        container.append(current_cart)
    return check_For_duplicate(container, item_name)
    
def displaySummary(container):
    print("------------------------- Cart Summary -----------------------------")
    Total_cost = 0
    for items in range(len(container)):
        current_item = container[items]
        cost_of_item_after_discounts = calculate_discount(current_item)
        Total_cost += cost_of_item_after_discounts 
        current_name = current_item["item_name"]
        current_price = current_item["item_price"]
        color = current_item["color"]
        weight = current_item["size"]
        print(f"item added: {items + 1}. {current_name} - Final Price: {current_price}(color = {color}, weight = {weight}kg)")

    print(f"Total cost = {Total_cost}")
        
print(displaySummary(user_response()))

