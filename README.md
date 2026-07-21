# 📦 Inventory Management System (Python)

A simple, console-based **Inventory Management System** built in core Python as a Lab Project for the **Programming Fundamentals (PF)** course, 2nd Semester, at **Superior University, Gold Campus, Lahore**.

The system lets a user add, view, update, delete, and search inventory items, and generates a quick summary of overall stock and value — all through a clean, menu-driven command line interface.

---

## 👥 Team Members

| Name | Roll No. |
|---|---|
| Haseeb Ahmad | 057 |
| Muhammad Ahsan | 056 |
| Muhammad Mujahid | - |

**Course:** Programming Fundamentals (PF) — Lab
**Semester:** 2nd Semester
**Tutor:** Sir Umair
**University:** Superior University, Gold Campus, Lahore

---

## 📖 About the Project

Manual inventory tracking using registers or spreadsheets is slow and error-prone. This project solves that problem with a lightweight Python application that stores inventory data in memory and lets the user perform all essential inventory operations through a simple text menu.

It was built to practice and demonstrate core Programming Fundamentals concepts: functions, loops, conditionals, lists, dictionaries, string formatting, and input validation with `try/except`.

---

## ✨ Features

- ➕ **Add Item** — add a new item with name, category, quantity, and price (auto-generated unique ID)
- 📋 **View All Items** — display the full inventory in a neatly aligned table
- ✏️ **Update Item** — update the quantity and/or price of an existing item by ID
- ❌ **Delete Item** — remove an item permanently by ID
- 🔍 **Search Item** — search items by name or category (case-insensitive, partial match)
- 📊 **Inventory Summary** — total items, total units in stock, total inventory value, most expensive item, and lowest stock item
- ✅ **Input Validation** — every numeric input is validated so the program never crashes on bad input

---

## 🛠️ Technology Used

| Component | Details |
|---|---|
| Language | Python 3 |
| Paradigm | Procedural / structured programming |
| Data Storage | In-memory (list of dictionaries) — no external database or file |
| Interface | Console / CLI, menu-driven |
| Dependencies | None — uses only the Python standard library |

---

## 🚀 Getting Started

### Prerequisites
- [Python 3](https://www.python.org/downloads/) installed on your machine

### Run the project
```bash
git clone https://github.com/<your-username>/inventory-management-system.git
cd inventory-management-system
python inventory_python.py
```

No additional packages need to be installed — the program runs with the Python standard library only.

---

## 🧭 How It Works

1. The program prints a header with the project and group details.
2. A main menu is displayed with 7 options (Add, View, Update, Delete, Search, Summary, Exit).
3. Based on the user's choice, the matching function runs and performs the requested operation.
4. All items are stored as dictionaries (`id`, `name`, `category`, `quantity`, `price`) inside a global list called `inventory`.
5. A global counter (`next_id`) auto-assigns a unique ID to every new item.
6. The loop keeps running until the user selects **Exit (7)**.

---

## 📂 Project Structure

```
inventory-management-system/
│
├── inventory_python.py     # Main application source code
└── README.md                # Project documentation (this file)
```

---

## 🔍 Function Overview

| Function | Purpose |
|---|---|
| `print_header()` | Displays project title and group information |
| `display_menu()` | Prints the main menu |
| `add_item()` | Adds a new item to the inventory |
| `view_items()` | Displays all items in a formatted table |
| `update_item()` | Updates quantity and/or price of an item |
| `delete_item()` | Deletes an item by ID |
| `search_item()` | Searches items by name or category |
| `inventory_summary()` | Shows overall inventory statistics |
| `main()` | Entry point; runs the menu loop |

---

## 📸 Sample Output

```
--------- MAIN MENU ---------
  1. Add Item
  2. View All Items
  3. Update Item
  4. Delete Item
  5. Search Item
  6. Inventory Summary
  7. Exit
-----------------------------
  Enter your choice (1-7): 1

--- ADD NEW ITEM ---
  Enter Item Name     : Rice Bag
  Enter Category      : Grocery
  Enter Quantity      : 50
  Enter Price (PKR)   : 3500

  [✓] 'Rice Bag' added successfully! (ID: 1)
```

---

## ✅ Advantages

- Lightweight — no external libraries required
- Simple, intuitive menu-driven interface
- Strong input validation prevents crashes
- Modular, function-based code that's easy to extend
- Cross-platform (Windows/macOS/Linux)

## ⚠️ Limitations

- Data resets every time the program closes (no persistent storage)
- Single-user only, no authentication
- Console-based only, no graphical interface

## 🔮 Future Enhancements

- [ ] Persistent storage using CSV/JSON or a database (SQLite/MySQL)
- [ ] Graphical user interface (Tkinter) or web interface (Flask/Django)
- [ ] User authentication and roles
- [ ] Export reports to PDF/Excel
- [ ] Low-stock alerts

---

## 📄 License

This project was developed for academic purposes as part of the Programming Fundamentals course at Superior University, Gold Campus, Lahore.

---

## 🙌 Acknowledgement

Special thanks to **Sir Umair** for his guidance throughout the Programming Fundamentals Lab course.
