"""This module provides functionality for managing temple data in Tamil Nadu.

The module includes functions for adding temples, removing temples, displaying
temples by city, deity, and dynasty, displaying temple features, counting 
temples by dynasty, and displaying a menu for user interaction.

The temple data is stored in a file using pickle for persistence.

Author: Dron Bhattachrya
"""
import pickle
import csv

temples_data = []


def save_data_to_file(temple_data):
    """
    Save the temple data to a file using pickle.

    Args:
        temple_data (object): The temple data to be saved.

    Returns:
        None
    """
    with open('temple_data.dat', 'wb') as f:
        pickle.dump(temple_data, f)


def add_temple():
    """
    Adds a new temple to the temples_data list.
    Prompts the user to enter temple details such as code, name,
    city, deity, dynasty, century, and remarks. Appends the temple
    details as a new list to the temples_data list.
    Saves the updated temples_data list to a file.
    """
    new_temple = {
        "code": input("Enter Temple Code: "),
        "name": input("Enter Temple Name: ").lower(),
        "city": input("Enter City Name: ").lower(),
        "deity": input("Enter Deity: ").lower(),
        "dynasty": input("Enter Dynasty: ").lower(),
        "century": input("Enter Century: ").lower(),
        "remark": input("Enter Remarks: ").lower()
    }

    temples_data.append(new_temple)
    save_data_to_file(temples_data)
    print("Temple data added successfully!")


def del_temple_by_code():
    """
    Deletes a temple from the temples_data list by code.
    Prompts the user to enter the code of the temple to be deleted.
    Deletes the temple from the temples_data list if it exists.
    Saves the updated temples_data list to a file.
    """
    code = input("Enter Temple Code: ")

    for temple in temples_data:
        if temple['code'] == code:
            temples_data.remove(temple)
            save_data_to_file(temples_data)
            print("Temple data removed successfully!")
            break
    else:
        print("Temple not found in the records.")


def display_temples_by_city():
    """Displays the temples based on the user input city name."""
    city_names = set(temple['city'] for temple in temples_data)
    print("Available City Names:", ", ".join(city_names))
    city_name = input("Enter City Name: ").lower()
    city_temples = [
        temple for temple in temples_data if temple['city'] == city_name]

    if city_temples:
        c = 1
        for temple in city_temples:
            print(
                f"{c}) Name: {temple['name']} || City: {temple['city']} || Deity: {temple['deity']}")
            c += 1
    else:
        print(f"No temples found for city {city_name}")


def display_temples_by_deity():
    """Displays the temples based on the deity name entered by the user."""
    deity_names = set(temple['deity'] for temple in temples_data)
    print("Available Deity Names:", ", ".join(deity_names))
    deity_name = input("Enter Deity Name: ").lower()
    deity_temples = [
        temple for temple in temples_data if temple['deity'] == deity_name]

    if deity_temples:
        c = 1
        for temple in deity_temples:
            print(
                f"{c}) Name: {temple['name']} || City: {temple['city']} || Deity: {temple['deity']}")
            c += 1
    else:
        print(f"No temples found for deity {deity_name}")


def display_temples_by_dynasty():
    """Displays the temples based on the dynasty name entered by the user."""
    dynasty_names = set(temple['dynasty'] for temple in temples_data)
    print("Available Dynasty Names:", ", ".join(dynasty_names))
    dynasty_name = input("Enter Dynasty Name: ").lower()
    dynasty_temples = [
        temple for temple in temples_data if temple['dynasty'] == dynasty_name]

    if dynasty_temples:
        c = 1
        for temple in dynasty_temples:
            print(
                f"{c}) Name: {temple['name']} || Dynasty: {temple['dynasty']} ")
            c += 1
    else:
        print(f"No temples found for dynasty {dynasty_name}")


def display_temple_features_by_name():
    """Displays the features of a temple based on the name entered by the user."""
    temple_names = set(temple['name'] for temple in temples_data)
    temple_name = input("Enter Temple Name: ").lower()
    if temple_name in temple_names:
        for temple in temples_data:
            if temple['name'] == temple_name:
                print(
                    f"{temple['name']} -- {temple['remark']}")
    else:
        print(f"No temple found with name {temple_name}")


def count_temples_for_given_dynasty():
    """Displays the number of temples for a given dynasty name."""
    dynasty_names = set(temple['dynasty'] for temple in temples_data)
    print("Available Dynasty Names:", ", ".join(dynasty_names))
    dynasty_name = input("Enter Dynasty Name: ").lower()
    dynasty_temples = [
        temple for temple in temples_data if temple['dynasty'] == dynasty_name]
    print(f"Total number of temples built: {len(dynasty_temples)}")


def count_temples_by_dynasty():
    """List the number of temples for each dynasty.
    """
    dynasty_names = set(temple['dynasty'] for temple in temples_data)
    for name in dynasty_names:
        dynasty_temples = [
            temple for temple in temples_data if temple['dynasty'] == name]
        print(f"{name} - {len(dynasty_temples)}")


def export_data():
    """Exports the temple data to a CSV or TXT file based on user input."""
    file_name = input("Enter the name of the file (without extension): ")
    export_format = input("Enter the export format (csv or txt): ").lower()

    if export_format == "csv":
        with open(f"{file_name}.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "City", "Deity", "Dynasty", "Remark"])
            for temple in temples_data:
                writer.writerow([temple["code"], temple["name"], temple["city"],
                                temple["deity"], temple["dynasty"], temple["remark"]])
        print(f"Data exported to {file_name}.csv")
    elif export_format == "txt":
        with open(f"{file_name}.txt", "w", encoding="utf-8") as f:
            for temple in temples_data:
                f.write(f"TCode: {temple['code']}\n")
                f.write(f"Name: {temple['name']}\n")
                f.write(f"City: {temple['city']}\n")
                f.write(f"Deity: {temple['deity']}\n")
                f.write(f"Dynasty: {temple['dynasty']}\n")
                f.write(f"Remark: {temple['remark']}\n")
                f.write("\n")
        print(f"Data exported to {file_name}.txt")
    else:
        print("Invalid export format. Please choose either csv or txt.")


def display_all_data():
    """Displays all the temple data."""
    for temple in temples_data:
        c = temple['code']
        nam = temple['name']
        ci = temple['city']
        de = temple['deity']
        dy = temple['dynasty']
        ce = temple['century']
        re = temple['remark']
        print(
            f"[Code: {c}]-[Name: {nam}]-[City: {ci}]-[Deity: {de}]-[Dynasty: {dy}]-[Century: {ce}]-[Remark: {re}]")


def display_menu():
    """Displays the menu for user interaction."""
    print("\nTamil Nadu Temple Database")
    print("\t1. Add a temple")
    print("\t2. Delete a temple")
    print("\t3. Display temples by city")
    print("\t4. Display temples by deity")
    print("\t5. Display temples by dynasty")
    print("\t6. Display temple features")
    print("\t7. Display dynasty and count")
    print("\t8. Count temples by dynasty")
    print("\t9. Export data to csv or txt file")
    print("\t10. Display all data")
    print("\t11. Exit")


# Load existing temple data if it exists
try:
    with open('temple_data.dat', 'rb') as file:
        temples_data = pickle.load(file)
except FileNotFoundError:
    temples_data = []

while True:
    display_menu()
    choice = int(input("[choice]->  "))

    if choice == 1:
        add_temple()
    elif choice == 2:
        del_temple_by_code()
    elif choice == 3:
        display_temples_by_city()
    elif choice == 4:
        display_temples_by_deity()
    elif choice == 5:
        display_temples_by_dynasty()
    elif choice == 6:
        display_temple_features_by_name()
    elif choice == 7:
        count_temples_for_given_dynasty()
    elif choice == 8:
        count_temples_by_dynasty()
    elif choice == 9:
        export_data()
    elif choice == 10:
        display_all_data()
    elif choice == 11:
        break
    else:
        print("Invalid choice. Please try again.")
