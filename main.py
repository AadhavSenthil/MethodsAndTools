from Inventory import Inventory
from Users import User
from shoppingcart import Cart

def main():
    inventory_instance = Inventory("inventory.db", "Inventory")
    # put your instances here; replace all ___ with instance
    user_instance = User("Users.db", "Users")
    cart_instance = Cart("ShoppingCart.db","Cart")

    while True:
        # user's getter for determining if user is logged in
        if user_instance.getLoggedIn() == False:
            print("\n1. Login")
            print("\n2. Create Account")
            print("\n3. Logout")

            choice = input("\nEnter your choice: ")
            if (choice == "1"):
                user_instance.login()
            elif (choice == "2"):
                user_instance.createAccount()
            elif (choice == "3"):
                user_instance.logout()
            else:
                print("\nInvalid choice. Please try again.")
        else:
            print("\n1. Logout")
            print("\n2. View Account Information") 
            print("\n3. Inventory Information")
            print("\n4. Cart Information")

            choice = input("\nEnter your choice: ")
            if (choice == "1"):
                user_instance.logout()
            elif (choice == "2"):
                user_instance.viewAccountInformation()
            elif (choice == "3"):
                inventory_menu(inventory_instance)
            elif (choice == "4"):
                cart_menu(cart_instance, user_instance, inventory_instance)
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
def cart_menu(cart_instance, user_instance, inventory_instance):
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
            cart_instance.view_cart(user_instance.getUserID(), inventory_instance.getDatabase())
        elif choice == "3":
            isbn_to_add = input("Enter the ISBN of the book to add to the cart: ")
            cart_instance.add_to_cart(user_instance.getUserID(), isbn_to_add)
        elif choice == "4":
            cart_instance.remove_from_cart(user_instance.getUserID())
        elif choice == "5":
            cart_instance.checkout(user_instance.getUserID(), inventory_instance)
        else:
            print("\nInvalid choice. Please try again.")

main()