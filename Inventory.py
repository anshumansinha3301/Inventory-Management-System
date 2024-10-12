import csv

# Inventory dictionary to store items and their details
inventory = {}

# Add item to the inventory
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

# Update item details
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

# Delete item from inventory
def delete_item():
    item_name = input("Enter the item name to delete: ").strip()
    if item_name in inventory:
        del inventory[item_name]
        print(f"{item_name} removed from the inventory.")
    else:
        print(f"{item_name} not found in the inventory.")

# View all items in the inventory with total value per item
def view_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for item_name, details in inventory.items():
            total_amount = details['quantity'] * details['price']
            print(f"Item: {item_name}, Quantity: {details['quantity']}, Price: ${details['price']:.2f}, Total Amount: ${total_amount:.2f}")
        print()

# Search for an item in the inventory
def search_item():
    item_name = input("Enter the item name to search: ").strip()
    if item_name in inventory:
        details = inventory[item_name]
        total_amount = details['quantity'] * details['price']
        print(f"Item: {item_name}, Quantity: {details['quantity']}, Price: ${details['price']:.2f}, Total Amount: ${total_amount:.2f}")
    else:
        print(f"{item_name} not found in the inventory.")

# Alert if item quantity is low
def restock_alert(threshold=5):
    alert_items = {item_name: details['quantity'] for item_name, details in inventory.items() if details['quantity'] <= threshold}
    if alert_items:
        print("Items that need restocking:")
        for item_name, quantity in alert_items.items():
            print(f"{item_name}: {quantity} units left")
    else:
        print("No items need restocking.")

# Calculate total inventory value
def calculate_total_value():
    total_value = sum(details['quantity'] * details['price'] for details in inventory.values())
    print(f"Total inventory value: ${total_value:.2f}")

# Export inventory to CSV file
def export_to_csv(filename="inventory_export.csv"):
    if not inventory:
        print("Inventory is empty, nothing to export.")
        return

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Item Name", "Quantity", "Price per Unit", "Total Amount"])
        for item_name, details in inventory.items():
            total_amount = details['quantity'] * details['price']
            writer.writerow([item_name, details['quantity'], details['price'], total_amount])

    print(f"Inventory exported to {filename}")

# Main function to manage inventory
def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Delete Item")
        print("4. View Inventory")
        print("5. Search for Item")
        print("6. Restock Alert")
        print("7. Calculate Total Inventory Value")
        print("8. Export Inventory to CSV")
        print("9. Exit")

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
            search_item()
        elif choice == '6':
            restock_alert()
        elif choice == '7':
            calculate_total_value()
        elif choice == '8':
            export_to_csv()
        elif choice == '9':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()