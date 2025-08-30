def add_item(current_cart: dict[str, int], items_to_add: tuple[str, ...]) -> dict[str, int]:
    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1

    return current_cart

def read_notes(notes) -> dict[str, int]:
    return dict.fromkeys(notes, 1)

def update_recipes(ideas: dict[str, dict[str, int]], recipe_updates) -> dict[str, dict[str, int]]:
    for recipe_name, new_ingredients in recipe_updates:
        ideas[recipe_name] = new_ingredients

    return ideas

def sort_entries(cart: dict[str, int]) -> dict[str, int]:
    return dict(sorted(cart.items()))

def send_to_store(cart: dict[str, int], aisle_mapping: dict[str, list[str, bool]]) -> dict[str, list[int, str, bool]]:
    
    for prod in cart:
        cart[prod] = [cart[prod]] + aisle_mapping[prod]
    
    return dict(reversed(sorted(cart.items())))

def update_store_inventory(fulfillment_cart: dict[str, list[int, str, bool]], store_inventory: dict[str, list[int, str, bool]]) -> dict[str, list[int | str, str, bool]]:
    
    for cart in store_inventory:
        if cart in fulfillment_cart:
            if store_inventory[cart][0] - fulfillment_cart[cart][0] == 0:
                store_inventory[cart][0] = 'Out of Stock'
            else:
                store_inventory[cart][0] = store_inventory[cart][0] - fulfillment_cart[cart][0]
            
    return store_inventory