import math

from datetime import datetime

from data import *


parking_records = load_data(PARKING_FILE)
payments = load_data(PAYMENTS_FILE)



malls = {

    "1": {
        "name": "Gateway Theatre of Shopping",
        "capacity": 250,
        "pricing": "flat"
    },

    "2": {
        "name": "Pavilion Shopping Centre",
        "capacity": 180,
        "pricing": "hourly"
    },

    "3": {
        "name": "La Lucia Mall",
        "capacity": 150,
        "pricing": "capped"
    }
}



def calculate_fee(pricing_type, hours):

    if pricing_type == "flat":
        return 15

    elif pricing_type == "hourly":
        return math.ceil(hours) * 10

    elif pricing_type == "capped":

        fee = math.ceil(hours) * 12

        if fee > 60:
            fee = 60

        return fee



def select_mall():

    print("\n===== SELECT MALL =====")

    for key, mall in malls.items():
        print(f"{key}. {mall['name']}")

    choice = input("Choose mall: ")

    if choice in malls:
        return malls[choice]

    print("Invalid mall selection")
    return None



def vehicle_entry(user):

    mall = select_mall()

    if mall is None:
        return

    current_vehicles = 0

    for record in parking_records:

        if (
            record["mall"] == mall["name"]
            and record["status"] == "parked"
        ):

            current_vehicles += 1

    if current_vehicles >= mall["capacity"]:
        print("Parking Full!")
        return

    vehicle = input("Enter vehicle registration: ")

    record = {

        "username": user["username"],
        "vehicle": vehicle,
        "mall": mall["name"],
        "pricing": mall["pricing"],
        "entry_time": str(datetime.now()),
        "exit_time": "",
        "hours": 0,
        "fee": 0,
        "status": "parked"
    }

    parking_records.append(record)

    save_data(PARKING_FILE, parking_records)

    print("Vehicle entry recorded!")



def vehicle_exit(user):

    vehicle = input("Enter vehicle registration: ")

    for record in parking_records:

        if (
            record["vehicle"] == vehicle
            and record["username"] == user["username"]
            and record["status"] == "parked"
        ):

            exit_time = datetime.now()

            entry_time = datetime.fromisoformat(
                record["entry_time"]
            )

            duration = exit_time - entry_time

            hours = duration.total_seconds() / 3600

            fee = calculate_fee(
                record["pricing"],
                hours
            )

            record["exit_time"] = str(exit_time)
            record["hours"] = round(hours, 2)
            record["fee"] = fee
            record["status"] = "awaiting payment"

            save_data(PARKING_FILE, parking_records)

            print("\n===== PARKING SUMMARY =====")
            print("Mall:", record["mall"])
            print("Duration:", round(hours, 2), "hours")
            print("Fee: R", fee)

            return

    print("Vehicle not found!")



def make_payment(user):

    vehicle = input("Enter vehicle registration: ")

    for record in parking_records:

        if (
            record["vehicle"] == vehicle
            and record["username"] == user["username"]
            and record["status"] == "awaiting payment"
        ):

            print("Outstanding Amount: R", record["fee"])

            confirm = input("Pay now? (yes/no): ")

            if confirm.lower() == "yes":

                payment = {

                    "username": user["username"],
                    "vehicle": vehicle,
                    "mall": record["mall"],
                    "amount": record["fee"],
                    "payment_time": str(datetime.now())
                }

                payments.append(payment)

                record["status"] = "completed"

                save_data(PAYMENTS_FILE, payments)
                save_data(PARKING_FILE, parking_records)

                print("Payment successful!")

                return

    print("No payment found!")



def view_history(user):

    print("\n===== HISTORY =====")

    found = False

    for record in parking_records:

        if record["username"] == user["username"]:

            found = True

            print("---------------------")
            print("Vehicle:", record["vehicle"])
            print("Mall:", record["mall"])
            print("Fee: R", record["fee"])
            print("Status:", record["status"])

    if not found:
        print("No history available")



def customer_menu(user):

    while True:

        print("\n===== CUSTOMER MENU =====")

        print("1. Vehicle Entry")
        print("2. Vehicle Exit")
        print("3. Make Payment")
        print("4. View History")
        print("5. Logout")

        choice = input("Choose option: ")

        if choice == "1":
            vehicle_entry(user)

        elif choice == "2":
            vehicle_exit(user)

        elif choice == "3":
            make_payment(user)

        elif choice == "4":
            view_history(user)

        elif choice == "5":
            break

        else:
            print("Invalid option")



def admin_menu(user):

    while True:

        print("\n===== ADMIN MENU =====")

        print("1. View Parked Vehicles")
        print("2. View Capacity")
        print("3. Logout")

        choice = input("Choose option: ")

        if choice == "1":

            for record in parking_records:

                if record["status"] == "parked":

                    print("-------------------")
                    print("Vehicle:", record["vehicle"])
                    print("Mall:", record["mall"])
                    print("Customer:", record["username"])

        elif choice == "2":

            for mall in malls.values():

                count = 0

                for record in parking_records:

                    if (
                        record["mall"] == mall["name"]
                        and record["status"] == "parked"
                    ):

                        count += 1

                print("-------------------")
                print(mall["name"])
                print("Capacity:", count, "/", mall["capacity"])

        elif choice == "3":
            break

        else:
            print("Invalid option")