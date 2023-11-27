from Inventory import Inventory

def main():
    inventory_instance = Inventory("inventory.db", "Inventory")
    # put your instances here; replace all ___ with instance

    while True:
        # user's getter for determining if user is logged in
        if getLoggedIn() == False:
            print("\n1. Login")
            print("\n2. Create Account")
            print("\n3. Logout")

            choice = input("\nEnter your choice: ")
            if (choice == "1"):
                ___.login()
            elif (choice == "2"):
                ___.createAccount()
            elif (choice == "3"):
                ___.logout()
            else:
                print("\nInvalid choice. Please try again.")
        else:
            print("\n1. Logout")
            print("\n2. View Account Information") 
            print("\n3. Inventory Information")
            print("\n4. Cart Information")

            choice = input("\nEnter your choice: ")
            if (choice == "1"):
                ___.logout()
            elif (choice == "2"):
                ___.viewAccountInformation()
            elif (choice == "3"):
                inventory_menu(inventory_instance)
            elif (choice == "4"):
                cart_menu(cart_instance)
            else:
                print("\nInvalid choice. Please try again.")


def inventory_menu(inventory_instance):
    while True:
        print("\n1. Go Back")
        print("\n2. View Inventory")
        print("\n3. Search Inventory")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            break
        elif choice == "2":
            inventory_instance.view_inventory()
        elif choice == "3":
            inventory_instance.search_inventory()
        else:
            print("\nInvalid choice. Please try again.")

# fix parameters or function/instance name to match cart 
def cart_menu(cart_instance):
    while True:
        print("\n1. Go Back")
        print("\n2. View Cart")
        print("\n3. Add Items to Cart")
        print("\n4. Remove an Item from Cart")
        print("\n5. Checkout")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            break
        elif choice == "2":
            cart_instance.view_cart()
        elif choice == "3":
            cart_instance.addToCart()
        elif choice == "4":
            cart_instance.removeFromCart()
        elif choice == "5":
            cart_instance.checkOut()
        else:
            print("\nInvalid choice. Please try again.")