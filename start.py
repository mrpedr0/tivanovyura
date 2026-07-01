from src.functions import get_all_users
from src.swapi import get_films, get_people, get_planets, get_species, get_vehicles, get_starships

exit = False

while not exit:
    print("\n--- Menu ---")
    print("1. Get all users")
    print("2. Films")
    print("3. People")
    print("4. Planets")
    print("5. Species")
    print("6. Vehicles")
    print("7. Starships")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        get_all_users()
    elif choice == '2':
        get_films()
    elif choice == '3':
        get_people()
    elif choice == '4':
        get_planets()
    elif choice == '5':
        get_species()
    elif choice == '6':
        get_vehicles()
    elif choice == '7':
        get_starships()
    elif choice == '0':
        exit = True
    else:
        print("Invalid choice. Please try again.")
