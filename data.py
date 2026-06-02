import json


USERS_FILE = "users.json"
PARKING_FILE = "parking_records.json"
PAYMENTS_FILE = "payments.json"


# LOAD DATA
def load_data(filename):

    try:
        with open(filename, "r") as file:
            return json.load(file)

    except:
        return []


# SAVE DATA
def save_data(filename, data):

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)