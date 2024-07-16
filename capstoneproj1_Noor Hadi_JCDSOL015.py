#data awal
list_player = [
    {
        "id": "LBFC240001",
        "name": "Ahmad Jaelani",
        "position": "Kiper",
        "country": "Indonesia",
        "age": 22,
        "wage": 12000000
    },
    {
        "id": "LBFC240002",
        "name": "Zulkarnaini",
        "position": "Anchor",
        "country": "Indonesia",
        "age": 29,
        "wage": 23000000
    },
    {
        "id": "LBFC240003",
        "name": "Rustam",
        "position": "Flank",
        "country": "Indonesia",
        "age": 19,
        "wage": 11000000
    },
    {
        "id": "LBFC240004",
        "name": "Tibo Tupamahu",
        "position": "Flank",
        "country": "Indonesia",
        "age": 20,
        "wage": 31000000
    },
    {
        "id": "LBFC240005",
        "name": "Leo Martinez",
        "position": "Pivot",
        "country": "Argentina",
        "age": 29,
        "wage": 91000000
    },
    {
        "id": "LBFC240006",
        "name": "Slavko Mirtiminiv",
        "position": "Flank",
        "country": "Russia",
        "age": 35,
        "wage": 12000000
    },
    {
        "id": "LBFC240007",
        "name": "Septo Maryono",
        "position": "Anchor",
        "country": "Indonesia",
        "age": 27,
        "wage": 39000000
    },
    {
        "id": "LBFC240008",
        "name": "David Silalahi",
        "position": "Flank",
        "country": "Indonesia",
        "age": 24,
        "wage": 16000000
    },
    {
        "id": "LBFC240009",
        "name": "Jonathan Albert",
        "position": "Flank",
        "country": "Indonesia",
        "age": 26,
        "wage": 37000000
    },
    {
        "id": "LBFC240010",
        "name": "Eko Sunjono",
        "position": "Kiper",
        "country": "Indonesia",
        "age": 35,
        "wage": 21000000
    }
]

#header footer
def display_header_footer():
    print("===== LUBUK BANGKU FUTSAL CLUB =====")
    print("~ together we can get everythings ~")
    print("Lubuk Bangku, Sumatera Barat- 26271")
    print()

#validasi id pemain
def validate_id(id):
    if len(id) != 10:
        return False
    if not id.startswith("LBFC"):
        return False
    try:
        int(id[4:])
    except ValueError:
        return False
    return True

#penetapan batas usia
def validate_age(age):
    if not (17 <= age <= 40):
        return False
    return True

#penetapan batas gaji
def validate_wage(wage):
    if not (10000000 <= wage <= 200000000):
        return False
    return True

#koreksi data duplikat berdasarkan ID
def check_duplicate_id(id):
    for player in list_player:
        if player['id'] == id:
            return True
    return False

#pembacaan seluruh pemain
def read_players():
    print("List of all players:")
    for player in list_player:
        print(f"ID: {player['id']}, Name: {player['name']}, Position: {player['position']}, Country: {player['country']}, Age: {player['age']}, Wage: {player['wage']}")

#pembacaan pemain berdasarkan id
def read_one_player():
    player_id = input("Enter player ID to read: ")
    for player in list_player:
        if player['id'] == player_id:
            print(f"Player details:")
            print(f"ID: {player['id']}, Name: {player['name']}, Position: {player['position']}, Country: {player['country']}, Age: {player['age']}, Wage: {player['wage']}")
            return
    print("Player ID not found!")

#validasi penambahan pemain
def create_player():
    print("Creating a new player...")
    while True:
        id = input("Enter player ID (must be 10 alphanumeric, starting with 'LBFC' and followed by 6 digits): ")
        if not validate_id(id):
            print("ID not valid. Please input 10 alphanumeric with first 4 as 'LBFC' and next 6 unique number.")
            continue
        if check_duplicate_id(id):
            print("ID already exists. Please enter a unique ID.")
            continue
        
        name = input("Enter player name: ")
        
        while True:
            position = input("Enter player position (Kiper, Flank, Anchor, Pivot): ")
            if position not in ["Kiper", "Flank", "Anchor", "Pivot"]:
                print("Invalid position. Please choose from 'Kiper', 'Flank', 'Anchor', 'Pivot'.")
                continue
            break
        
        country = input("Enter player country: ")
        
        while True:
            try:
                age = int(input("Enter player age (between 17 and 40): "))
                if not validate_age(age):
                    print("Age must be between 17 and 40.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        while True:
            try:
                wage = int(input("Enter player wage (between 10,000,000 and 200,000,000): "))
                if not validate_wage(wage):
                    print("Wage must be between 10,000,000 and 200,000,000.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        new_player = {
            "id": id,
            "name": name,
            "position": position,
            "country": country,
            "age": age,
            "wage": wage
        }
        
        print("\nNew Player Details:")
        print(f"ID: {id}, Name: {name}, Position: {position}, Country: {country}, Age: {age}, Wage: {wage}")
        confirm = input("Are the data correct? (1. Yes / 2. No): ")
        if confirm == "1":
            list_player.append(new_player)
            print("Player added successfully!")
            break
        else:
            print("Please re-enter player details.\n")

#konfirmasi penambahan pemain
def update_player():
    player_id = input("Enter player ID to update: ")
    for player in list_player:
        if player['id'] == player_id:
            print(f"Updating player: {player['name']}")
            
            while True:
                position = input("Enter new position (Kiper, Flank, Anchor, Pivot): ")
                if position not in ["Kiper", "Flank", "Anchor", "Pivot"]:
                    print("Invalid position. Please choose from 'Kiper', 'Flank', 'Anchor', 'Pivot'.")
                    continue
                player["position"] = position
                break
            
            while True:
                try:
                    player["wage"] = int(input("Enter new wage: "))
                    if not validate_wage(player["wage"]):
                        print("Wage must be between 10,000,000 and 200,000,000.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
            
            print("\nUpdated Player Details:")
            print(f"ID: {player['id']}, Name: {player['name']}, Position: {player['position']}, Country: {player['country']}, Age: {player['age']}, Wage: {player['wage']}")
            confirm = input("Are the data correct? (1. Yes / 2. No): ")
            if confirm == "1":
                print("Player updated successfully!")
                return
            else:
                print("Update canceled. Reverting changes...\n")
                return
    
    print("Player ID not found!")

#konfirmasi hapus pemain
def delete_player():
    while True:
        player_id = input("Enter player ID to delete: ")
        for index, player in enumerate(list_player):
            if player['id'] == player_id:
                print(f"Deleting player:")
                print(f"ID: {player['id']}, Name: {player['name']}, Position: {player['position']}, Country: {player['country']}, Age: {player['age']}, Wage: {player['wage']}")
                confirm = input("Are you sure to delete this player? (1. Yes / 2. No): ")
                if confirm == "1":
                    del list_player[index]
                    print("Player deleted successfully!")
                    return
                else:
                    print("Deletion canceled.\n")
                    return
        print("Player ID not found!")
        input("\nPress Enter to continue...")

#looping
if __name__ == "__main__":
    while True:
        display_header_footer()
        print("MENU:")
        print("A. Read Players")
        print("B. Create Player")
        print("C. Update Player")
        print("D. Delete Player")
        print("E. Exit")

        choice = input("Enter your choice (A, B, C, D, E): ").upper()

        if choice == "A":
            print("1. Read All Players")
            print("2. Read One Player")
            print("3. Back to Main Menu")
            read_choice = input("Enter your choice (1, 2, 3): ")
            if read_choice == "1":
                read_players()
            elif read_choice == "2":
                read_one_player()
            elif read_choice == "3":
                continue
        
        elif choice == "B":
            print("1. Add New Player")
            print("2. Back to Main Menu")
            create_choice = input("Enter your choice (1, 2): ")
            if create_choice == "1":
                create_player()
            elif create_choice == "2":
                continue
        
        elif choice == "C":
            print("1. Update Player from List")
            print("2. Back to Main Menu")
            update_choice = input("Enter your choice (1, 2): ")
            if update_choice == "1":
                update_player()
            elif update_choice == "2":
                continue
        
        elif choice == "D":
            print("1. Delete Player from List")
            print("2. Back to Main Menu")
            delete_choice = input("Enter your choice (1, 2): ")
            if delete_choice == "1":
                delete_player()
            elif delete_choice == "2":
                continue
        
        elif choice == "E":
            print("Exiting Program")
            print("~ Thank You ~")
            break
        
        else:
            print("Invalid choice! Please enter a valid option.")
        
        input("\nPress Enter to Main Menu")
