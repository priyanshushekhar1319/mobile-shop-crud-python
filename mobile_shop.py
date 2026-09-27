mobiles = []

def add_mobile():
    mobile_id = int(input("Enter Mobile ID: "))
    for mobile in mobiles:
        if mobile[0] == mobile_id:
            print("ID already exists")
            return
    brand = input("Enter Brand: ")
    model = input("Enter Model: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))
    mobiles.append([mobile_id, brand, model, price, quantity])
    print("Mobile added successfully")

def display_mobiles():
    if not mobiles:
        print("No mobiles available")
        return
    for mobile in mobiles:
        print(mobile)

def search_mobile():
    mobile_id = int(input("Enter Mobile ID: "))
    for mobile in mobiles:
        if mobile[0] == mobile_id:
            print(mobile)
            return
    print("Mobile not found")

def update_mobile():
    mobile_id = int(input("Enter Mobile ID: "))
    for mobile in mobiles:
        if mobile[0] == mobile_id:
            mobile[1] = input("Enter Brand: ")
            mobile[2] = input("Enter Model: ")
            mobile[3] = float(input("Enter Price: "))
            mobile[4] = int(input("Enter Quantity: "))
            print("Mobile updated")
            return
    print("Mobile not found")

def delete_mobile():
    mobile_id = int(input("Enter Mobile ID: "))
    for mobile in mobiles:
        if mobile[0] == mobile_id:
            if input("Delete? (Y/N): ").upper() == "Y":
                mobiles.remove(mobile)
                print("Mobile deleted")
            return
    print("Mobile not found")

def dashboard():
    while True:
        print("\n1. Add Mobile")
        print("2. Display All Mobiles")
        print("3. Search Mobile")
        print("4. Update Mobile")
        print("5. Delete Mobile")
        print("6. Exit")
        choice = input("Enter choice: ")

        match choice:
            case "1":
                add_mobile()
            case "2":
                display_mobiles()
            case "3":
                search_mobile()
            case "4":
                update_mobile()
            case "5":
                delete_mobile()
            case "6":
                break
            case _:
                print("Invalid choice")

dashboard()
