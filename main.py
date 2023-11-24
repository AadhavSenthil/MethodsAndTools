from Inventory import Inventory

def main():
    inventory_instance = Inventory("inventory.db", "Inventory")
    # put your instances here

    while True:
        # user's getter for determining if user is logged in
        if getLoggedIn() == False:
            print("\n1. Login")
            print("\n2. Create Account")
            print("\n3. Logout")

            choice = input("Enter your choice: ")
            if (choice == "1"):
            elif (choice == "2"):
            elif (choice == "3"):
            else:
                print("Invalid choice. Please try again.")
        else:
            print("\n1. Logout")
            print("\n2. View Account Information") 
            print("\n3. Inventory Information")
            print("\n4. Cart Information")

            choice = input("Enter your choice: ")
            if (choice == "1"):
            elif (choice == "2"):
            elif (choice == "3"):
                inventory_menu(inventory_instance)
            elif (choice == "4"):
                cart_menu(cart_instance)
            else:
                print("Invalid choice. Please try again.")


def inventory_menu(inventory_instance):
    while True:
        print("\nAfter Login (Inventory Information):")
        print("\n1. Go Back")
        print("\n2. View Inventory")
        print("\n3. Search Inventory")
        choice = input("Enter your choice: ")

        if choice == "1":
            break
        elif choice == "2":
            inventory_instance.view_inventory()
        elif choice == "3":
            inventory_instance.search_inventory()
        else:
            print("Invalid choice. Please try again.")