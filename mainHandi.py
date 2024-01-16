import pickle

data=[]

def save_data(data):
    with open("data.dat", "wb") as file:
        pickle.dump(data, file)

def add_handicraft():
    global data
    item = {
        "code": input("Enter handicraft code: "),
        "name": input("Enter handicraft name: "),
        "type": input("Enter handicraft type: "),
        "area": input("Enter area of origin: "),
        "material": input("Enter material used: "),
        "price": int(input("Enter price: ")),
        "remark": input("Enter remarks: ")
    }
    data.append(item)
    save_data(data)
    print("Handicraft data added successfully!")

def del_handi():
    global data
    code = input("Enter handicraft code: ")
    rmHandi = []
    for handi in data:
        if handi["code"] == code:
            rmHandi = handi
            break
    removed_handi = [
        handi for handi in data if handi["code"] != code]

    if len(removed_handi) == len(data):
        print("No matching handicraft found for removal.")
    else:
        data = removed_handi
        save_data(data)

        print("removed successfully: ", rmHandi)

def display_name_price_by_area():
    area_names = set(handi["area"] for handi in data)
    print("Available Area Names:", area_names)
    area_name = input("Enter Area Name: ")
    area_handis = [
        handi for handi in data if handi["area"] == area_name]

    if area_handis:
        for handi in area_handis:
            print(
                f"Handicraft Name: {handi['name']}, Price: {handi['price']}")
    else:
        print(f"No handicrafts found in {area_name}")

def display_saree_items():
    saree_handis = [
        handi for handi in data if handi["type"] == "Saree"]

    if saree_handis:
        for handi in saree_handis:
            print(
                    f"Name: {handi['name']}, Material:{handi['material']}, Price: {handi['price']}")
    else:
        print(f"No sarees found")

def display_brass_items():
    brass_handis = [
        handi for handi in data if handi["material"] == "Brass"]

    if brass_handis:
        for handi in brass_handis:
            print(
                    f"Name: {handi['name']}, Area:{handi['area']}, Price: {handi['price']}")
    else:
        print(f"No brass handicrafts found")

def count_items_from_Thanjavur():
    thanjavur_handis = [
        handi for handi in data if handi["area"] == "Thanjavur"]

    if thanjavur_handis:
        print(f"Number of handicrafts from Thanjavur: {len(thanjavur_handis)}")
    else:
        print(f"No handicrafts found from Thanjavur")

def display_avg_price_of_saree():
    saree_handis = [
        handi for handi in data if handi["type"] == "Saree"]

    if saree_handis:
        total = 0
        for handi in saree_handis:
            total += handi["price"]
        print(f"Average price of sarees: {total/len(saree_handis)}")
    else:
        print(f"No sarees found")

def max_price_of_sculpture_type():
    sculpture_handis = [
        handi for handi in data if handi["type"] == "Sculpture"]

    if sculpture_handis:
        max_price = sculpture_handis[0]["price"]
        for handi in sculpture_handis:
            if handi["price"] > max_price:
                max_price = handi["price"]
        print(f"Maximum price of sculpture type: {max_price}")
    else:
        print(f"No sculpture handicrafts found")


def PrintData():
    print("Format: Code || Name || Type || Area || Material || Price || Remark\n")
    for handi in data:
        print(f"{handi['code']} || {handi['name']} || {handi['type']} || {handi['area']} || {handi['material']} || {handi['price']} || {handi['remark']}")
    print("\n")

def loadData():
    global data
    try:
        with open("data.dat", "rb") as file:
            data = pickle.load(file)
    except:
        data = []

def display_menu():
    print("Menu Options are:")
    print("\t1. Add Handicraft")
    print("\t2. Delete Handicraft")
    print("\t3. Display Name and Price by Area")
    print("\t4. Display Saree Items")
    print("\t5. Display Brass Items")
    print("\t6. Count Items from Thanjavur")
    print("\t7. Display Average Price of Saree")
    print("\t8. Display Maximum Price of Sculpture Type")
    print("\t9. Display all data")
    print("\t10. Exit")

loadData()

while True:
    display_menu()
    choice = input("choice> ")

    if choice == '1':
        add_handicraft()
    elif choice == '2':
        del_handi()
    elif choice == '3':
        display_name_price_by_area()
    elif choice == '4':
        display_saree_items()
    elif choice == '5':
        display_brass_items()
    elif choice == '6':
        count_items_from_Thanjavur()
    elif choice == '7':
        display_avg_price_of_saree()
    elif choice == '8':
        max_price_of_sculpture_type()
    elif choice == '9':
        PrintData()
    elif choice == '10':
        break
    else:
        print("Invalid choice. Please try again.")
