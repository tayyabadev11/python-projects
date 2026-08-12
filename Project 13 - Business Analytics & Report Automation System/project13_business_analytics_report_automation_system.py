import csv
import json
import logging
import re
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
# -------------------- Project Setup --------------------
DATA_FOLDER = Path("business_analytics_data")
DATA_FOLDER.mkdir(exist_ok=True)
JSON_FILE = DATA_FOLDER / "sales_data.json"
CSV_FILE = DATA_FOLDER / "sales_report.csv"
REPORT_FILE = DATA_FOLDER / "business_report.txt"
LOG_FILE = DATA_FOLDER / "application.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
# -------------------- Data Model --------------------

@dataclass
class Sale:
    product: str
    category: str
    quantity: int
    price: float
    salesperson: str
    email: str

    @property
    def revenue(self):
        return self.quantity * self.price


# -------------------- Sample Business Data --------------------

sales = [
    Sale("Laptop Stand", "Accessories", 8, 4500, "Alex Carter", "alex@example.com"),
    Sale("Wireless Mouse", "Accessories", 15, 2800, "Morgan Lee", "morgan@example.com"),
    Sale("Keyboard", "Accessories", 10, 4200, "Jordan Smith", "jordan@example.com"),
    Sale("Webcam", "Electronics", 6, 8500, "Taylor Brown", "taylor@example.com"),
    Sale("USB Hub", "Electronics", 20, 2200, "Casey Wilson", "casey@example.com"),
]


# -------------------- Validation --------------------

def validate_email(email: str) -> bool:
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))


def validate_sales_data(records):
    for sale in records:
        if sale.quantity <= 0 or sale.price < 0:
            raise ValueError("Invalid quantity or price detected.")

        if not validate_email(sale.email):
            raise ValueError(f"Invalid email format: {sale.email}")


# -------------------- Calculations --------------------

def calculate_total_revenue(*records):
    return sum(sale.revenue for sale in records)


def calculate_average_revenue(records):
    if not records:
        return 0

    return calculate_total_revenue(*records) / len(records)


def get_top_products(records, limit=3):
    return sorted(
        records,
        key=lambda sale: sale.revenue,
        reverse=True
    )[:limit]


def get_category_summary(records):
    summary = {}

    for sale in records:
        summary[sale.category] = summary.get(sale.category, 0) + sale.revenue

    return summary


# -------------------- Data Storage --------------------

def save_json(records):
    data = [asdict(sale) | {"revenue": sale.revenue} for sale in records]

    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    logging.info("Sales data saved to JSON.")


def save_csv(records):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "product",
                "category",
                "quantity",
                "price",
                "salesperson",
                "email",
                "revenue"
            ]
        )

        writer.writeheader()

        for sale in records:
            writer.writerow(asdict(sale) | {"revenue": sale.revenue})

    logging.info("Sales report exported to CSV.")


# -------------------- Business Report --------------------

def generate_report(records):
    total_revenue = calculate_total_revenue(*records)
    average_revenue = calculate_average_revenue(records)
    category_summary = get_category_summary(records)
    top_products = get_top_products(records)

    report_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(REPORT_FILE, "w", encoding="utf-8") as file:
        file.write("BUSINESS ANALYTICS REPORT\n")
        file.write("=" * 40 + "\n")
        file.write(f"Generated: {report_time}\n\n")

        file.write(f"Total Sales Records: {len(records)}\n")
        file.write(f"Total Revenue: Rs. {total_revenue:,.2f}\n")
        file.write(f"Average Sale: Rs. {average_revenue:,.2f}\n\n")

        file.write("CATEGORY PERFORMANCE\n")
        file.write("-" * 40 + "\n")

        for category, revenue in category_summary.items():
            file.write(f"{category}: Rs. {revenue:,.2f}\n")

        file.write("\nTOP PRODUCTS\n")
        file.write("-" * 40 + "\n")

        for index, sale in enumerate(top_products, start=1):
            file.write(
                f"{index}. {sale.product} - "
                f"Rs. {sale.revenue:,.2f}\n"
            )

    logging.info("Business report generated.")


# -------------------- Display --------------------

def display_dashboard(records):
    total_revenue = calculate_total_revenue(*records)
    average_revenue = calculate_average_revenue(records)
    category_summary = get_category_summary(records)

    print("\n" + "=" * 55)
    print("        BUSINESS ANALYTICS DASHBOARD")
    print("=" * 55)

    print(f"Total Sales Records : {len(records)}")
    print(f"Total Revenue       : Rs. {total_revenue:,.2f}")
    print(f"Average Sale        : Rs. {average_revenue:,.2f}")

    print("\nCategory Performance")
    print("-" * 55)

    for category, revenue in category_summary.items():
        print(f"{category:<20} Rs. {revenue:,.2f}")

    print("\nTop Performing Products")
    print("-" * 55)

    for index, sale in enumerate(get_top_products(records), start=1):
        print(
            f"{index}. {sale.product:<20} "
            f"Rs. {sale.revenue:,.2f}"
        )

    print("=" * 55)


# -------------------- Main Application --------------------

def main():
    print("\nWelcome to Business Analytics & Report Automation System")
    try:
        validate_sales_data(sales)
        save_json(sales)
        save_csv(sales)
        generate_report(sales)
        display_dashboard(sales)
        print("\nFiles generated successfully:")
        print(f"- JSON Data    : {JSON_FILE}")
        print(f"- CSV Report   : {CSV_FILE}")
        print(f"- Text Report  : {REPORT_FILE}")
        print(f"- Activity Log : {LOG_FILE}")
        print("\nBusiness analysis completed successfully.")
        logging.info("Application completed successfully.")
    except (ValueError, OSError) as error:
        print(f"\nUnable to complete the operation: {error}")
        logging.error(f"Application error: {error}")
if __name__ == "__main__":
    main()
