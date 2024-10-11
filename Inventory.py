# Inventory dictionary to store items and their details
inventory = {}

def add_item():
    item_name = input("Enter the item name: ").strip()
    if item_name in inventory:
        print(f"{item_name} is already in the inventory.")
        return
    
    try:
        quantity = int(input("Enter the quantity: "))
        price = float(input("Enter the price per unit: "))
    except ValueError:
        print("Invalid input for quantity or price.")
        return
    
    inventory[item_name] = {"quantity": quantity, "price": price}
    print(f"{item_name} added to the inventory.")

def update_item():
    item_name = input("Enter the item name to update: ").strip()
    if item_name not in inventory:
        print(f"{item_name} not found in the inventory.")
        return
    
    try:
        quantity = int(input("Enter the new quantity: "))
        price = float(input("Enter the new price per unit: "))
    except ValueError:
        print("Invalid input for quantity or price.")
        return
    
    inventory[item_name] = {"quantity": quantity, "price": price}
    print(f"{item_name} updated successfully.")

def delete_item():
    item_name = input("Enter the item name to delete: ").strip()
    if item_name in inventory:
        del inventory[item_name]
        print(f"{item_name} removed from the inventory.")
    else:
        print(f"{item_name} not found in the inventory.")

def view_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for item_name, details in inventory.items():
            print(f"Item: {item_name}, Quantity: {details['quantity']}, Price: ${details['price']:.2f}")
        print()

def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Delete Item")
        print("4. View Inventory")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            add_item()
        elif choice == '2':
            update_item()
        elif choice == '3':
            delete_item()
        elif choice == '4':
            view_inventory()
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
