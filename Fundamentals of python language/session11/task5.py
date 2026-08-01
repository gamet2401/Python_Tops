def update_cart(cart, item, qty):
    cart[item] = qty   
    return cart

cart = {"Shoes": 1, "T-shirt": 2}
cart = update_cart(cart, "Shoes", 3)       
cart = update_cart(cart, "Jeans", 1)      
print(cart)
