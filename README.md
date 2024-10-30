### Software Requirements Specification (SRS) for Basic Inventory Management System

The **Basic Inventory Management System** is a simple console-based application designed to help small businesses or individual users manage their inventory. The system allows users to add, update, delete, and view inventory items efficiently, providing a streamlined process for managing stock levels and item information. The system is intended to be user-friendly and requires no prior experience in inventory management.

The system provides functionality for adding items to the inventory, where users input the item's name, quantity, and price per unit. Each item is stored in a dictionary structure, ensuring quick access and modification. In the event that a user attempts to add an item that already exists, the system prevents duplication by notifying the user. The **Update Item** functionality allows users to adjust the quantity and price of an existing item in the inventory, ensuring that stock levels and pricing are accurate and up to date.

For items that are no longer in stock or no longer needed, the **Delete Item** feature allows users to remove items from the inventory entirely. This ensures that the inventory remains clutter-free and reflects only the currently available items. The system also includes an option to **View Inventory**, which displays all the items, their quantities, and respective prices. This view gives users a clear snapshot of their current stock levels and overall inventory status.

The system is designed with simplicity in mind, providing easy navigation through a menu interface. It operates without any additional dependencies or external databases, making it lightweight and accessible in any Python environment. The application is ideal for users who need a straightforward and efficient way to manage their inventory without the complexities of larger, more advanced systems.
(Open Source Project for Hacktoberfest2024)
