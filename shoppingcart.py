import sqlite3

class Cart:
    def __init__(self, databaseName, tableName):
        self.databaseName = databaseName
        self.tableName = tableName

    def view_cart(self, userID, inventoryDatabase):
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()

        # Retrieve cart items for the given user
        cursor.execute(f"SELECT ISBN FROM {self.tableName} WHERE UserID = ?", (userID,))
        cart_items = cursor.fetchall()

        if not cart_items:
            print("Cart is empty.")
        else:
            print("Books in Cart:")
            for isbn in cart_items:
                book_info = inventoryDatabase.getBookInfoByISBN(isbn[0])
                if book_info:
                    print(f"ISBN: {isbn[0]}, Title: {book_info['Title']}, Stock: {book_info['Stock']}")
                else:
                    print(f"ISBN: {isbn[0]} (Book information not found in inventory)")

    def add_to_cart(self, userID, ISBN):
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()

        # Check if the item is already in the cart
        cursor.execute(f"SELECT * FROM {self.tableName} WHERE UserID = ? AND ISBN = ?", (userID, ISBN))
        existing_item = cursor.fetchone()

        if existing_item:
            print("Item is already in the cart.")
        else:
            # Add the item to the cart
            cursor.execute(f"INSERT INTO {self.tableName} (UserID, ISBN) VALUES (?, ?)", (userID, ISBN))
            connection.commit()
            print(f"Book with ISBN: {ISBN} added to the cart!")

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

        # Retrieve cart items for the given user
        cursor.execute(f"SELECT ISBN FROM {self.tableName} WHERE UserID = ?", (userID,))
        cart_items = cursor.fetchall()

        if not cart_items:
            print("Cart is empty. There is nothing to check out.")
        else:
            total_price = 0

            # Calculate total price and update inventory
            for isbn in cart_items:
                book_info = inventoryDatabase.get_book_info_by_isbn(isbn[0])
                if book_info:
                    total_price += book_info['Price']
                    inventoryDatabase.decreaseStock(isbn[0])
                else:
                    print(f"ISBN: {isbn[0]} (Book information not found in inventory)")

            # Clear the cart
            cursor.execute(f"DELETE FROM {self.tableName} WHERE UserID = ?", (userID,))
            connection.commit()

            print(f"Checkout successful. Total Price: ${total_price:.2f}")
