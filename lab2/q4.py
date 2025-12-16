inventory = {"apple": 10, "banana": 5, "milk": 2}

while True:
    print("\n1. Add Item\n2. Sell Item\n3. Show Low Stock\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Item name: ")
        qty = int(input("Quantity: "))
        if item in inventory:
            inventory[item] += qty
        else:
            inventory[item] = qty
        print("Updated Inventory:", inventory)

    elif choice == "2":
        item = input("Item name: ")
        qty = int(input("Quantity to sell: "))
        if item in inventory and inventory[item] >= qty:
            inventory[item] -= qty
            print("Updated Inventory:", inventory)
        else:
            print("Not enough stock or item does not exist.")

    elif choice == "3":
        low_stock = {k: v for k, v in inventory.items() if v < 3}
        print("Low Stock Items:", low_stock)

    elif choice == "4":
        break

    else:
        print("Invalid choice")
