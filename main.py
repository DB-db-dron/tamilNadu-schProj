import pickle

temples_data = []

def save_temple_data(temple_data):
    with open('temple_data.pkl', 'wb') as file:
        pickle.dump(temple_data, file)


def add_temple():
    global temples_data
    code = input("Enter Temple Code: ")
    name = input("Enter Temple Name: ")
    city = input("Enter City Name: ")
    deity = input("Enter Deity: ")
    dynasty = input("Enter Dynasty: ")
    century = input("Enter Century: ")
    remark = input("Enter Remarks: ")

    new_temple = [code, name, city, deity, dynasty, century, remark]
    temples_data.append(new_temple)
    save_temple_data(temples_data)
    print("Temple data added successfully!")


def remove_temple():
    global temples_data
    tcode = input("Enter Temple id to remove: ")
    rmTemple = []
    for temple in temples_data:
        if temple[0] == tcode:
            rmTemple = temple
            break
    removed_temples = [
        temple for temple in temples_data if temple[0] != tcode]

    if len(removed_temples) == len(temples_data):
        print("No matching temple found for removal.")
    else:
        temples_data = removed_temples
        save_temple_data(temples_data)

        print("removed successfully: ", rmTemple)

def display_temples_by_city():
    city_names = set(temple[2] for temple in temples_data)
    print("Available City Names:", city_names)
    city_name = input("Enter City Name: ")
    city_temples = [
        temple for temple in temples_data if temple[2] == city_name]

    if city_temples:
        for temple in city_temples:
            print(
                f"Temple Name: {temple[1]}, City: {temple[2]}, Deity: {temple[3]}")
    else:
        print(f"No temples found in {city_name}")


def display_temples_by_deity():
    deity_names = set(temple[3] for temple in temples_data)
    print("Available Deity Names:", deity_names)
    deity_name = input("Enter Deity Name: ")
    deity_temples = [
        temple for temple in temples_data if temple[3] == deity_name]

    if deity_temples:
        print(f"Temples for deity {deity_name}:")
        for temple in deity_temples:
            print(
                f"Temple Name: {temple[1]}, City: {temple[2]}, Deity: {temple[3]}")
    else:
        print(f"No temples found for deity {deity_name}")


def display_temples_by_dynasty():
    dynasty_names = set(temple[4] for temple in temples_data)
    print("Available Dynasty Names:", dynasty_names)
    dynasty_name = input("Enter Dynasty Name: ")
    dynasty_temples = [(temple[1], temple[4])
                       for temple in temples_data if temple[4] == dynasty_name]

    if dynasty_temples:
        for temple in dynasty_temples:
            print(f"Temple Name: {temple[0]}, Dynasty: {temple[1]}")
    else:
        print(f"No temples found for dynasty {dynasty_name}")


def display_temple_features():
    temple_name = input("Enter Temple Name: ")
    found = False

    for temple in temples_data:
        if temple[1] == temple_name:
            print(f"Temple Name: {temple[1]}")
            print(f"Special Features: {temple[6]}")
            found = True
            break

    if not found:
        print("Temple not found in the records.")


def display_dynasty_and_count():
    dynasty_names = set(temple[4] for temple in temples_data)
    print("Available Dynasty Names:", dynasty_names)
    dynasty_name = input("Enter Dynasty Name: ")
    dynasty_temples = [
        temple for temple in temples_data if temple[4] == dynasty_name]

    if dynasty_temples:
        print(f"Total Temples for dynasty {dynasty_name}: {len(dynasty_temples)}")
    else:
        print(f"No temples found for dynasty {dynasty_name}")


def count_temples_by_dynasty():
    dynasty_names = set(temple[4] for temple in temples_data)

    print("Total Temples built by each dynasty:")
    for name in dynasty_names:
        count = 0
        for temple in temples_data:
            if temple[4] == name:
                count += 1
        print(f"{name}: {count}")


def display_menu():
    print("\nTemple Data Management")
    print("\t1. Add Temple")
    print("\t2. Remove Temple")
    print("\t3. Display Temples for a given City")
    print("\t4. Display Temples for a given Deity")
    print("\t5. Display Temples for a given Dynasty")
    print("\t6. Display features for given temple")
    print("\t7. Count number of temples for a given dynasty")
    print("\t8. Count number of temples for each dynasty")
    print("\t9. Exit")


# Load existing temple data if it exists
try:
    with open('temple_data.pkl', 'rb') as file:
        temples_data = pickle.load(file)
except FileNotFoundError:
    temples_data = []

while True:
    display_menu()
    choice = input("choice> ")

    if choice == '1':
        add_temple()
    elif choice == '2':
        remove_temple()
    elif choice == '3':
        display_temples_by_city()
    elif choice == '4':
        display_temples_by_deity()
    elif choice == '5':
        display_temples_by_dynasty()
    elif choice == '6':
        display_temple_features()
    elif choice == '7':
        display_dynasty_and_count()
    elif choice == '8':
        count_temples_by_dynasty()
    elif choice == '9':
        print("Exiting program...")
        save_temple_data(temples_data)
        break
    else:
        print("Invalid choice. Please enter a valid option.")
