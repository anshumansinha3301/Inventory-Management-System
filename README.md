### Software Requirements Specification (SRS) for Basic Inventory Management System

**Inventory Management System Documentation**

## Introduction
The **Inventory Management System** is a Python-based application that helps manage stock efficiently. It allows users to add, update, delete, search, and export inventory records while providing alerts for low stock levels.

## Features
1. **Add Items** – Insert new items into the inventory.
2. **Update Items** – Modify existing item details.
3. **Delete Items** – Remove items from inventory.
4. **View Inventory** – Display all items with quantities, prices, and total values.
5. **Search for Items** – Find specific items in the inventory.
6. **Restock Alerts** – Notify users when item quantities fall below a defined threshold.
7. **Calculate Total Inventory Value** – Compute the overall worth of stock.
8. **Export to CSV** – Save inventory records to a CSV file.

## Usage Guide

### 1. **Adding an Item**
- Users are prompted to enter an item name, quantity, and price per unit.
- The system ensures duplicate items are not added.
- The item is stored in the inventory dictionary.

### 2. **Updating an Item**
- Users can modify the quantity and price of an existing item.
- The system checks for the item's existence before allowing updates.

### 3. **Deleting an Item**
- Users enter the item name to remove it from inventory.
- The system verifies whether the item exists before deletion.

### 4. **Viewing Inventory**
- Displays all stored items, their quantities, unit prices, and total worth.
- If inventory is empty, a notification is displayed.

### 5. **Searching for an Item**
- Allows users to find an item by name and view its details.
- If the item is not found, a notification is provided.

### 6. **Restock Alerts**
- Items with a quantity less than or equal to 5 are flagged.
- A list of such items is displayed.

### 7. **Calculating Total Inventory Value**
- Computes and displays the total monetary value of all stored items.

### 8. **Exporting Inventory to CSV**
- Saves inventory records to a CSV file with item name, quantity, price per unit, and total amount.
- If the inventory is empty, an appropriate message is displayed.

## Error Handling
- **Invalid Inputs:** Ensures numerical values are entered for quantity and price.
- **Item Existence Checks:** Prevents duplicate additions and ensures updates/deletions are valid.

## Running the Application
1. Run the script using
   ```bash
   python inventory.py
   ```
3. Follow the menu prompts to perform inventory operations.
4. Exit the application by selecting option `9`.

## Conclusion
This system provides an easy-to-use solution for managing inventory efficiently, ensuring stock levels are maintained and properly recorded.


(Open Source Project for Hacktoberfest2024)
