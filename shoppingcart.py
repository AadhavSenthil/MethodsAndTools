import sqlite3

class Cart:
    def __init__(self, databaseName, tableName):
        self.databaseName = databaseName
        self.tableName = tableName

    def view_cart(self, userID, inventoryDatabase):
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()

        # Retrieve cart items for the given user
        cursor.execute(f"SELECT ISBN, Quantity FROM {self.tableName} WHERE UserID = ?", (userID,))
        cart_items = cursor.fetchall()

        if not cart_items:
            print("Cart is empty.")
        else:
            print("Books in Cart:")
            for isbn, quantity in cart_items:
                # Use the updated method for getting book information
                book_info = inventoryDatabase.get_book_info_by_isbn(isbn)
                if book_info:
                    print(f"ISBN: {isbn}, Title: {book_info['Title']}, Quantity: {quantity}")
                else:
                    print(f"ISBN: {isbn} (Book information not found in inventory)")

    def add_to_cart(self, userID, ISBN, inventory_instance):
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()

        # Check if the item is already in the cart
        cursor.execute(f"SELECT * FROM {self.tableName} WHERE UserID = ? AND ISBN = ?", (userID, ISBN))
        existing_item = cursor.fetchone()

        if existing_item:
            # If the item already exists, update the quantity
            cursor.execute(f"UPDATE {self.tableName} SET Quantity = Quantity + 1 WHERE UserID = ? AND ISBN = ?", (userID, ISBN))
            connection.commit()
            print(f"Book with ISBN: {ISBN} quantity updated in the cart.")
        else:
            # Check if the ISBN exists in the inventory
            if inventory_instance.get_book_info_by_isbn(ISBN):
                # Add the item to the cart with a default quantity (or adjust as needed)
                cursor.execute(f"INSERT INTO {self.tableName} (UserID, ISBN, Quantity) VALUES (?, ?, 1)", (userID, ISBN))
                connection.commit()
                print(f"Book with ISBN: {ISBN} added to the cart!")
            else:
                print(f"Book with ISBN: {ISBN} does not exist in the inventory.")

    def remove_from_cart(self, userID, ISBN):
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()

        # Remove the item from the cart
        cursor.execute(f"DELETE FROM {self.tableName} WHERE UserID = ? AND ISBN = ?", (userID, ISBN))
        connection.commit()
        print(f"Book with ISBN: {ISBN} removed from the cart!")

    def checkout(self, userID, inventoryDatabase):
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()

        # Retrieve cart items for the given user with quantity
        cursor.execute(f"SELECT ISBN, Quantity FROM {self.tableName} WHERE UserID = ?", (userID,))
        cart_items = cursor.fetchall()

        if not cart_items:
            print("Cart is empty. There is nothing to check out.")
        else:
            total_price = 0

            # Calculate total price and update inventory
            for isbn, quantity in cart_items:
                book_info = inventoryDatabase.get_book_info_by_isbn(isbn)
                if book_info:
                    total_price += book_info['Price'] * quantity
                    inventoryDatabase.decreaseStock(isbn, quantity)  # Pass quantity as a third argument
                else:
                    print(f"ISBN: {isbn} (Book information not found in inventory)")

            # Clear the cart
            cursor.execute(f"DELETE FROM {self.tableName} WHERE UserID = ?", (userID,))
            connection.commit()

            print(f"Checkout successful. Total Price: ${total_price:.2f}")
