
products = {
    "Keyboard": {"price": 1500, "stock": 10},
    "Mouse": {"price": 800, "stock": 15},
    "Monitor": {"price": 15000, "stock": 5}
}

cart = []

print("=== RABIN STORE ===")
print("\nAvailable products:")

for name, details in products.items():
    print(name, "| Price: Rs.", details["price"], "| Stock:", details["stock"])

# Customer selects multiple products
selected_products = input(
    "\nWhich products would you like to buy? "
    "(Separate names with commas): "
)

selected_products = selected_products.split(",")

for product in selected_products:
    product_name = product.strip().title()

    if product_name not in products:
        print(f"Sorry, {product_name} is not available in our store.")
        continue

    available_stock = products[product_name]["stock"]

    if available_stock == 0:
        print(f"Sorry, {product_name} is out of stock.")
        continue

    try:
        quantity = int(input(f"How many {product_name}s do you want? "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        if quantity > available_stock:
            print(
                f"Sorry, you requested {quantity}, "
                f"but we only have {available_stock} available."
            )

            answer = input(
                "Would you like to buy all the remaining stock? (yes/no): "
            ).strip().lower()

            if answer in ("yes", "y"):
                quantity = available_stock
            elif answer in ("no", "n"):
                print("No problem! Let's continue with your other products.")
                continue
            else:
                print("Invalid answer. This product will be skipped.")
                continue

        total = products[product_name]["price"] * quantity
        products[product_name]["stock"] -= quantity

        cart.append({
            "product": product_name,
            "quantity": quantity,
            "total": total
        })

        print(f"Added {quantity} {product_name}(s) to your cart.")

    except ValueError:
        print("Invalid quantity. Please enter a whole number.")

# Final bill
print("\n=== YOUR FINAL BILL ===")

grand_total = 0

for item in cart:
    print(
        item["product"],
        "| Quantity:", item["quantity"],
        "| Total: Rs.", item["total"]
    )
    grand_total += item["total"]

print("Grand total: Rs.", grand_total)
print("Thank you for visiting Rabin Store!")
