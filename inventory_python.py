# ============================================================
#        INVENTORY MANAGEMENT SYSTEM
#        Course    : Programming Fundamentals (PF)
#        Semester  : 2nd Semester
#        University: Superior University, Gold Campus, Lahore
#        Tutor     : Sir Umair
#        Members   : 1) Haseeb Ahmad
#                    2) Mujahid
#                    3) Ahsan
# ============================================================

# ---------- Global Inventory List ----------
inventory = []
next_id = 1  # Auto-increment ID for each item

# ============================================================
#  FUNCTION: Print Project Header
# ============================================================
def print_header():
    print("=" * 60)
    print("       INVENTORY MANAGEMENT SYSTEM")
    print("=" * 60)
    print("  Course    : Programming Fundamentals (PF)")
    print("  Semester  : 2nd Semester")
    print("  University: Superior University, Gold Campus")
    print("  Tutor     : Sir Umair")
    print("  Members   : 1) Haseeb Ahmad 057")
    print("              2) Mujahid")
    print("              3) Ahsan 056")
    print("=" * 60)
    print()

# ============================================================
#  FUNCTION: Display Main Menu
# ============================================================
def display_menu():
    print("\n--------- MAIN MENU ---------")
    print("  1. Add Item")
    print("  2. View All Items")
    print("  3. Update Item")
    print("  4. Delete Item")
    print("  5. Search Item")
    print("  6. Inventory Summary")
    print("  7. Exit")
    print("-----------------------------")

# ============================================================
#  FUNCTION: Add New Item to Inventory
# ============================================================
def add_item():
    global next_id
    print("\n--- ADD NEW ITEM ---")
    name     = input("  Enter Item Name     : ").strip()
    category = input("  Enter Category      : ").strip()

    # Input validation for quantity
    while True:
        qty = input("  Enter Quantity      : ").strip()
        if qty.isdigit():
            qty = int(qty)
            break
        else:
            print("  [!] Please enter a valid whole number for quantity.")

    # Input validation for price
    while True:
        try:
            price = float(input("  Enter Price (PKR)   : ").strip())
            break
        except ValueError:
            print("  [!] Please enter a valid number for price.")

    # Create item as dictionary
    item = {
        "id"      : next_id,
        "name"    : name,
        "category": category,
        "quantity": qty,
        "price"   : price
    }

    inventory.append(item)
    next_id += 1
    print(f"\n  [✓] '{name}' added successfully! (ID: {item['id']})")

# ============================================================
#  FUNCTION: View All Inventory Items
# ============================================================
def view_items():
    print("\n--- INVENTORY LIST ---")
    if len(inventory) == 0:
        print("  [!] No items in inventory yet.")
        return

    # Table Header
    print(f"\n  {'ID':<5} {'Name':<20} {'Category':<15} {'Qty':<8} {'Price (PKR)':<12}")
    print("  " + "-" * 62)

    # Table Rows
    for item in inventory:
        print(f"  {item['id']:<5} {item['name']:<20} {item['category']:<15} {item['quantity']:<8} {item['price']:<12.2f}")

    print("  " + "-" * 62)

# ============================================================
#  FUNCTION: Update an Existing Item
# ============================================================
def update_item():
    print("\n--- UPDATE ITEM ---")
    if len(inventory) == 0:
        print("  [!] No items to update.")
        return

    view_items()

    while True:
        try:
            item_id = int(input("\n  Enter Item ID to Update: "))
            break
        except ValueError:
            print("  [!] Please enter a valid ID number.")

    # Search for item by ID
    found = None
    for item in inventory:
        if item["id"] == item_id:
            found = item
            break

    if found is None:
        print("  [!] Item with this ID not found.")
        return

    print(f"\n  Updating: {found['name']}")
    print("  What do you want to update?")
    print("    1. Quantity")
    print("    2. Price")
    print("    3. Both")
    choice = input("  Enter choice (1/2/3): ").strip()

    if choice == "1" or choice == "3":
        while True:
            qty = input("  New Quantity: ").strip()
            if qty.isdigit():
                found["quantity"] = int(qty)
                break
            else:
                print("  [!] Invalid quantity.")

    if choice == "2" or choice == "3":
        while True:
            try:
                found["price"] = float(input("  New Price (PKR): ").strip())
                break
            except ValueError:
                print("  [!] Invalid price.")

    print(f"  [✓] Item '{found['name']}' updated successfully!")

# ============================================================
#  FUNCTION: Delete an Item from Inventory
# ============================================================
def delete_item():
    print("\n--- DELETE ITEM ---")
    if len(inventory) == 0:
        print("  [!] No items to delete.")
        return

    view_items()

    while True:
        try:
            item_id = int(input("\n  Enter Item ID to Delete: "))
            break
        except ValueError:
            print("  [!] Please enter a valid ID number.")

    for i in range(len(inventory)):
        if inventory[i]["id"] == item_id:
            deleted_name = inventory[i]["name"]
            inventory.pop(i)
            print(f"  [✓] '{deleted_name}' deleted successfully!")
            return

    print("  [!] Item with this ID not found.")

# ============================================================
#  FUNCTION: Search Item by Name or Category
# ============================================================
def search_item():
    print("\n--- SEARCH ITEM ---")
    if len(inventory) == 0:
        print("  [!] No items in inventory.")
        return

    keyword = input("  Enter name or category to search: ").strip().lower()
    results = []

    for item in inventory:
        if keyword in item["name"].lower() or keyword in item["category"].lower():
            results.append(item)

    if len(results) == 0:
        print(f"  [!] No items found for '{keyword}'.")
    else:
        print(f"\n  Found {len(results)} result(s):\n")
        print(f"  {'ID':<5} {'Name':<20} {'Category':<15} {'Qty':<8} {'Price (PKR)':<12}")
        print("  " + "-" * 62)
        for item in results:
            print(f"  {item['id']:<5} {item['name']:<20} {item['category']:<15} {item['quantity']:<8} {item['price']:<12.2f}")

# ============================================================
#  FUNCTION: Show Inventory Summary / Stats
# ============================================================
def inventory_summary():
    print("\n--- INVENTORY SUMMARY ---")
    if len(inventory) == 0:
        print("  [!] No items in inventory.")
        return

    total_items    = len(inventory)
    total_quantity = 0
    total_value    = 0.0
    most_expensive = inventory[0]
    lowest_stock   = inventory[0]

    for item in inventory:
        total_quantity += item["quantity"]
        total_value    += item["quantity"] * item["price"]
        if item["price"] > most_expensive["price"]:
            most_expensive = item
        if item["quantity"] < lowest_stock["quantity"]:
            lowest_stock = item

    print(f"\n  Total Unique Items  : {total_items}")
    print(f"  Total Units in Stock: {total_quantity}")
    print(f"  Total Inventory Value: PKR {total_value:,.2f}")
    print(f"  Most Expensive Item : {most_expensive['name']} (PKR {most_expensive['price']:.2f})")
    print(f"  Lowest Stock Item   : {lowest_stock['name']} (Qty: {lowest_stock['quantity']})")

# ============================================================
#  MAIN PROGRAM — Entry Point
# ============================================================
def main():
    print_header()

    while True:
        display_menu()
        choice = input("  Enter your choice (1-7): ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            view_items()
        elif choice == "3":
            update_item()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            search_item()
        elif choice == "6":
            inventory_summary()
        elif choice == "7":
            print("\n  Thank you for using the Inventory Management System!")
            print("  Developed by: Haseeb Ahmad, Mujahid & Ahsan")
            print("  Superior University, Gold Campus — 2nd Semester\n")
            break
        else:
            print("  [!] Invalid choice. Please enter a number between 1 and 7.")

# Run the program
main()
