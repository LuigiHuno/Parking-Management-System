from users import *
from parking import *
from reports import *


while True:

    print("\n===================================")
    print("   PARKING MANAGEMENT SYSTEM")
    print("===================================")

    print("1. Customer")
    print("2. Parking Administrator")
    print("3. Owner/Shareholder")
    print("4. Exit")

    choice = input("Select option: ")

    
    if choice == "1":

        while True:

            print("\n===== CUSTOMER SECTION =====")
            print("1. Register")
            print("2. Login")
            print("3. Back")

            option = input("Choose option: ")

            if option == "1":
                register_customer()

            elif option == "2":

                customer = login("customer")

                if customer:
                    customer_menu(customer)

            elif option == "3":
                break

            else:
                print("Invalid option")

    
    elif choice == "2":

        admin = login("admin")

        if admin:
            admin_menu(admin)

    
    elif choice == "3":

        owner = login("owner")

        if owner:
            owner_reports()

    
    elif choice == "4":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid option")