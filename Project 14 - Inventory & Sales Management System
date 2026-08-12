import json
import csv
import logging
from datetime import datetime
from pathlib import Path
# ============================================================
# PROJECT 14 - INVENTORY & SALES MANAGEMENT SYSTEM
# ============================================================

DATA_DIR = Path("inventory_sales_data")
DATA_DIR.mkdir(exist_ok=True)

PRODUCTS_FILE = DATA_DIR / "products.json"
SALES_FILE = DATA_DIR / "sales.json"
REPORT_FILE = DATA_DIR / "sales_report.csv"
LOG_FILE = DATA_DIR / "application.log"


# ============================================================
# LOGGING SETUP
# ============================================================

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ============================================================
# SAMPLE PRODUCTS
# ============================================================

sample_products = [
    {
        "id": 1001,
        "name": "Wireless Mouse",
        "category": "Accessories",
        "price": 3500,
        "stock": 15
    },
    {
        "id": 1002,
        "name": "USB Hub",
        "category": "Accessories",
        "price": 4500,
        "stock": 10
    },
    {
        "id": 1003,
        "name": "Webcam",
        "category": "Electronics",
        "price": 12000,
        "stock": 8
    },
    {
        "id": 1004,
        "name": "Keyboard",
        "category": "Accessories",
        "price": 5500,
        "stock": 12
    },
    {
        "id": 1005,
        "name": "Headphones",
        "category": "Audio",
        "price": 7500,
        "stock": 6
    }
]


# ============================================================
# LOAD DATA
# ============================================================

def load_data(file_path, default_data):
    try:
        if file_path.exists():
            with open(file_path, "r") as file:
                return json.load(file)

        with open(file_path, "w") as file:
            json.dump(default_data, file, indent=4)

        return default_data

    except Exception as error:
        logging.error(f"Error loading data: {error}")
        return default_data


products = load_data(PRODUCTS_FILE, sample_products)
sales = load_data(SALES_FILE, [])


# ============================================================
# SAVE DATA
# ============================================================

def save_products():
    with open(PRODUCTS_FILE, "w") as file:
        json.dump(products, file, indent=4)


def save_sales():
    with open(SALES_FILE, "w") as file:
        json.dump(sales, file, indent=4)


# ============================================================
# VIEW INVENTORY
# ============================================================

def view_inventory():
    print("\n" + "=" * 65)
    print("INVENTORY DIRECTORY")
    print("=" * 65)

    for product in products:
        print(f"ID       : {product['id']}")
        print(f"Name     : {product['name']}")
        print(f"Category : {product['category']}")
        print(f"Price    : Rs. {product['price']:,.2f}")
        print(f"Stock    : {product['stock']}")
        print("-" * 65)


# ============================================================
# ADD PRODUCT
# ============================================================

def add_product():
    print("\n--- Add New Product ---")

    try:
        product_id = int(input("Enter product ID: "))
        name = input("Enter product name: ")
        category = input("Enter category: ")
        price = float(input("Enter price: "))
        stock = int(input("Enter stock quantity: "))

        new_product = {
            "id": product_id,
            "name": name,
            "category": category,
            "price": price,
            "stock": stock
        }

        products.append(new_product)
        save_products()

        logging.info(f"New product added: {name}")

        print("\n✓ Product added successfully.")

    except ValueError:
        print("\n✗ Please enter valid numeric values.")
        logging.error("Invalid product input.")


# ============================================================
# SEARCH PRODUCT
# ============================================================

def search_product():
    print("\n--- Search Product ---")

    keyword = input("Enter product name or category: ").lower()

    found = False

    for product in products:
        if (
            keyword in product["name"].lower()
            or keyword in product["category"].lower()
        ):
            print("\nProduct Found")
            print(f"ID       : {product['id']}")
            print(f"Name     : {product['name']}")
            print(f"Category : {product['category']}")
            print(f"Price    : Rs. {product['price']:,.2f}")
            print(f"Stock    : {product['stock']}")

            found = True

    if not found:
        print("\n✗ No matching product found.")


# ============================================================
# RECORD SALE
# ============================================================

def record_sale():
    print("\n--- Record Sale ---")

    try:
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity sold: "))

        for product in products:

            if product["id"] == product_id:

                if quantity <= 0:
                    print("\n✗ Quantity must be greater than zero.")
                    return

                if quantity > product["stock"]:
                    print("\n✗ Not enough stock available.")
                    return

                total = product["price"] * quantity

                product["stock"] -= quantity

                sale = {
                    "product_id": product["id"],
                    "product_name": product["name"],
                    "quantity": quantity,
                    "total": total,
                    "date": datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                }

                sales.append(sale)

                save_products()
                save_sales()

                logging.info(
                    f"Sale recorded: {product['name']} x {quantity}"
                )

                print("\n✓ Sale recorded successfully.")
                print(f"Product : {product['name']}")
                print(f"Quantity: {quantity}")
                print(f"Total   : Rs. {total:,.2f}")

                return

        print("\n✗ Product ID not found.")

    except ValueError:
        print("\n✗ Please enter valid numbers.")


# ============================================================
# SALES SUMMARY
# ============================================================

def sales_summary():
    print("\n" + "=" * 65)
    print("SALES SUMMARY")
    print("=" * 65)

    if not sales:
        print("No sales recorded yet.")
        return

    total_sales = len(sales)
    total_units = sum(sale["quantity"] for sale in sales)
    total_revenue = sum(sale["total"] for sale in sales)

    print(f"Total Sales Transactions : {total_sales}")
    print(f"Total Units Sold         : {total_units}")
    print(f"Total Revenue            : Rs. {total_revenue:,.2f}")

    print("\nSales History")
    print("-" * 65)

    for sale in sales:
        print(
            f"{sale['product_name']} | "
            f"Qty: {sale['quantity']} | "
            f"Rs. {sale['total']:,.2f} | "
            f"{sale['date']}"
        )


# ============================================================
# GENERATE CSV REPORT
# ============================================================

def generate_csv_report():
    if not sales:
        print("\n✗ No sales available for report.")
        return

    try:
        with open(REPORT_FILE, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Product ID",
                "Product Name",
                "Quantity",
                "Total",
                "Date"
            ])

            for sale in sales:
                writer.writerow([
                    sale["product_id"],
                    sale["product_name"],
                    sale["quantity"],
                    sale["total"],
                    sale["date"]
                ])

        print("\n✓ Sales report created successfully.")
        print(f"Report file: {REPORT_FILE}")

        logging.info("CSV sales report generated.")

    except Exception as error:
        print("\n✗ Error creating report.")
        logging.error(f"CSV report error: {error}")


# ============================================================
# LOW STOCK REPORT
# ============================================================

def low_stock_report():
    print("\n" + "=" * 65)
    print("LOW STOCK REPORT")
    print("=" * 65)

    low_stock_products = [
        product for product in products
        if product["stock"] <= 5
    ]

    if not low_stock_products:
        print("✓ No products have critically low stock.")
        return

    for product in low_stock_products:
        print(
            f"{product['name']} "
            f"-> Remaining Stock: {product['stock']}"
        )


# ============================================================
# MAIN MENU
# ============================================================

def main():

    print("\n" + "=" * 65)
    print("      INVENTORY & SALES MANAGEMENT SYSTEM")
    print("=" * 65)

    while True:

        print("\n1. View Inventory")
        print("2. Add New Product")
        print("3. Search Product")
        print("4. Record Sale")
        print("5. Sales Summary")
        print("6. Generate CSV Report")
        print("7. Low Stock Report")
        print("8. Exit")

        print("=" * 65)

        choice = input("Select an option: ")

        if choice == "1":
            view_inventory()

        elif choice == "2":
            add_product()

        elif choice == "3":
            search_product()

        elif choice == "4":
            record_sale()

        elif choice == "5":
            sales_summary()

        elif choice == "6":
            generate_csv_report()

        elif choice == "7":
            low_stock_report()

        elif choice == "8":
            print("\n✓ Thank you for using Inventory & Sales Management System.")
            logging.info("Application closed.")
            break

        else:
            print("\n✗ Invalid option. Please select 1-8.")


# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":
    main()
