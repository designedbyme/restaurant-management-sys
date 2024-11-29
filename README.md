# restaurant-management-sys

the program is meant to run our interpretation of a restaurant management system

**User Interface (GUI):**
Use a GUI framework such as Tkinter (or PyQt) to create a user-friendly interface.
_Main components_:
  Table Management: 
    Display available tables, occupied tables, and table status (e.g., seated, ordered, served).
  Menu Display: 
    Section for displaying menu items, organized by categories (e.g., appetizers, main course, beverages, desserts).
  Order Management: 
    Area where servers can add menu items to each table’s order, adjust quantities, and view the running total.
  Order Summary: 
    Display of selected items for a particular table with details like item name, quantity, unit price, and subtotal.
  Billing Section: 
    Display the total bill, tax, and any discounts applied.
  Control Buttons: 
    Buttons for submitting orders, updating orders, clearing tables, and generating bills.

**Table and Order Management:**
Table Assignment: 
  Allow servers to assign orders to specific tables and mark tables as occupied or vacant.
Order Taking: 
  For each table, enable users to select items from the menu, specify quantities, and add items to the current order.
Order Editing: 
  Allow servers to modify the order by adding or removing items before submitting it.
Order Status:
  Display and update the status of each table’s order (e.g., ordered, in preparation, served, paid).
Clear Table:
  Clear a table’s status once the bill is paid, making it available for new customers.
