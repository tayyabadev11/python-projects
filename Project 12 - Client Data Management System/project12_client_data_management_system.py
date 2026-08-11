import csv
import json
import logging
import os
import re
import shutil
from collections import Counter
from datetime import datetime
from pathlib import Path
# Application folders and files
BASE_DIR = Path("client_management_data")
BACKUP_DIR = BASE_DIR / "backups"

JSON_FILE = BASE_DIR / "clients.json"
CSV_FILE = BASE_DIR / "clients_report.csv"
LOG_FILE = BASE_DIR / "application.log"


BASE_DIR.mkdir(exist_ok=True)
BACKUP_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
# Default sample records
sample_clients = [
    {
        "id": 1001,
        "name": "Alex Morgan",
        "email": "alex@example.com",
        "service": "Website Development",
        "status": "Active",
        "created_at": "2026-08-11 09:00:00"
    },
    {
        "id": 1002,
        "name": "Jordan Lee",
        "email": "jordan@example.com",
        "service": "Data Analysis",
        "status": "Completed",
        "created_at": "2026-08-11 09:10:00"
    },
    {
        "id": 1003,
        "name": "Taylor Smith",
        "email": "taylor@example.com",
        "service": "Automation",
        "status": "Pending",
        "created_at": "2026-08-11 09:20:00"
    }
]


def initialize_data():
    if not JSON_FILE.exists():
        JSON_FILE.write_text(
            json.dumps(sample_clients, indent=4),
            encoding="utf-8"
        )
        logging.info("Initial client data created.")


def load_clients():
    try:
        data = JSON_FILE.read_text(encoding="utf-8")

        if not data.strip():
            return []

        return json.loads(data)

    except (json.JSONDecodeError, OSError) as error:
        logging.error("Unable to load client data: %s", error)
        print("Unable to load the client data.")
        return []


def save_clients(clients):
    try:
        JSON_FILE.write_text(
            json.dumps(clients, indent=4),
            encoding="utf-8"
        )
        logging.info("Client data saved successfully.")

    except OSError as error:
        logging.error("Unable to save client data: %s", error)
        print("Unable to save the client data.")


def display_clients(clients):
    if not clients:
        print("\nNo client records are available.")
        return

    print("\n" + "=" * 78)
    print("CLIENT DIRECTORY")
    print("=" * 78)

    for client in clients:
        print(f"ID      : {client['id']}")
        print(f"Name    : {client['name']}")
        print(f"Email   : {client['email']}")
        print(f"Service : {client['service']}")
        print(f"Status  : {client['status']}")
        print(f"Created : {client['created_at']}")
        print("-" * 78)


def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


def add_client(clients):
    print("\n--- Add New Client ---")

    name = input("Enter client name: ").strip()
    email = input("Enter client email: ").strip()
    service = input("Enter requested service: ").strip()

    if not name or not service:
        print("Name and service are required.")
        return

    if not validate_email(email):
        print("Please enter a valid email address.")
        return

    new_id = max((client["id"] for client in clients), default=1000) + 1

    new_client = {
        "id": new_id,
        "name": name,
        "email": email,
        "service": service,
        "status": "Pending",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    clients.append(new_client)
    save_clients(clients)

    logging.info("New client added with ID %s.", new_id)

    print("\n✓ Client record added successfully.")
    print(f"✓ Client ID: {new_id}")


def search_client(clients):
    keyword = input("\nEnter name, email, or service to search: ").strip().lower()

    results = [
        client
        for client in clients
        if keyword in client["name"].lower()
        or keyword in client["email"].lower()
        or keyword in client["service"].lower()
    ]

    if results:
        display_clients(results)
        logging.info("Client search completed for keyword: %s", keyword)
    else:
        print("\nNo matching client records were found.")


def generate_report(clients):
    if not clients:
        print("\nThere are no records available for reporting.")
        return

    status_count = Counter(client["status"] for client in clients)
    service_count = Counter(client["service"] for client in clients)

    print("\n" + "=" * 50)
    print("CLIENT PERFORMANCE REPORT")
    print("=" * 50)

    print(f"Total Clients: {len(clients)}")

    print("\nStatus Summary:")
    for status, count in status_count.items():
        print(f"- {status}: {count}")

    print("\nService Summary:")
    for service, count in service_count.items():
        print(f"- {service}: {count}")

    logging.info("Client performance report generated.")


def export_csv(clients):
    try:
        with CSV_FILE.open("w", newline="", encoding="utf-8") as file:
            fieldnames = [
                "id",
                "name",
                "email",
                "service",
                "status",
                "created_at"
            ]

            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(clients)

        logging.info("Client data exported to CSV.")
        print(f"\n✓ CSV report created: {CSV_FILE}")

    except OSError as error:
        logging.error("CSV export failed: %s", error)
        print("Unable to create the CSV report.")


def create_backup():
    try:
        if not JSON_FILE.exists():
            print("\nNo client data is available for backup.")
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = BACKUP_DIR / f"clients_backup_{timestamp}.json"

        shutil.copy2(JSON_FILE, backup_file)

        logging.info("Backup created: %s", backup_file)
        print("\n✓ Client data backup created successfully.")
        print(f"✓ Backup file: {backup_file}")

    except OSError as error:
        logging.error("Backup creation failed: %s", error)
        print("Unable to create the backup.")


def show_system_info():
    try:
        file_size = os.path.getsize(JSON_FILE)

        print("\n" + "=" * 50)
        print("SYSTEM INFORMATION")
        print("=" * 50)
        print(f"Data Directory : {BASE_DIR}")
        print(f"Data File      : {JSON_FILE}")
        print(f"Data Size      : {file_size} bytes")
        print(f"Log File       : {LOG_FILE}")
        print(f"Current Time   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        logging.info("System information viewed.")

    except OSError as error:
        logging.error("Unable to read system information: %s", error)
        print("System information is currently unavailable.")


def main():
    initialize_data()
    clients = load_clients()

    logging.info("Client management application started.")

    while True:
        print("\n" + "=" * 60)
        print("        CLIENT DATA MANAGEMENT SYSTEM")
        print("=" * 60)
        print("1. View Client Directory")
        print("2. Add New Client")
        print("3. Search Client")
        print("4. Generate Performance Report")
        print("5. Export CSV Report")
        print("6. Create Data Backup")
        print("7. View System Information")
        print("8. Exit")
        print("=" * 60)

        choice = input("Select an option: ").strip()

        if choice == "1":
            display_clients(clients)

        elif choice == "2":
            add_client(clients)
            clients = load_clients()

        elif choice == "3":
            search_client(clients)

        elif choice == "4":
            generate_report(clients)

        elif choice == "5":
            export_csv(clients)

        elif choice == "6":
            create_backup()

        elif choice == "7":
            show_system_info()

        elif choice == "8":
            logging.info("Application closed successfully.")
            print("\nThank you for using the Client Data Management System.")
            print("Session completed successfully.")
            break

        else:
            print("\nInvalid option. Please select a number from 1 to 8.")
            logging.warning("Invalid menu option selected: %s", choice)

if __name__ == "__main__":
    main()
