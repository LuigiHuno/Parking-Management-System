from parking import *


def owner_reports():

    print("\n===== OWNER REPORTS =====")

    for mall in malls.values():

        total_vehicles = 0
        total_revenue = 0
        total_hours = 0

        for record in parking_records:

            if record["mall"] == mall["name"]:

                total_vehicles += 1
                total_revenue += record["fee"]
                total_hours += record["hours"]

        average_duration = 0

        if total_vehicles > 0:
            average_duration = (
                total_hours / total_vehicles
            )

        print("\n====================")
        print("Mall:", mall["name"])
        print("Vehicles:", total_vehicles)
        print("Revenue: R", total_revenue)
        print(
            "Average Duration:",
            round(average_duration, 2),
            "hours"
        )