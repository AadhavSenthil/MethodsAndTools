
class Cart:
    # Constructor
    def __init__(self):
        pass
    
    #Initial set up
    def __init__(self, dataBaseName, tableName):
        self.dataBaseName = dataBaseName
        self.tableName = tableName

    # View cart function
    def viewCart(self, userID, inventoryDatabase):
        # gets all of the cart items
        cart_items = self.getCartItems(userID)
        print("Books in Cart: ")

        # iterates through all of the ISBNs for viewing
        for isbn in cart_items:
            bookInfo = inventoryDatabase.getBookInfoByISBN(isbn)
            print(f"ISBN: {isbn}, Title: {bookInfo['title']}, Price: {bookInfo['price']}")

    def addToCart(self, userID, ISBN):
        # Function that has been yet to be created but it will add the ISBN to the cart by userID
        User.addToCart(userID, ISBN)

        print(f"Book with ISBN: {ISBN} added to the cart!")

    
    def removeFromCart(self, userID, ISBN):
        # No idea what the name is for this yet
        User.removeFromCart(userID, ISBN)

        print(f"Book with ISBN: {ISBN} removed from the cart!")

    def checkOut(self, userID, inventoryDatabase):
        # Gets the cart items from userID
        cart_items = self.getCartItems(userID)

        # If the cart is empty then this is displayed
        if not cart_items:
            print("Cart is empty. There is nothing to check out.")

        # initial price set
        total_price = 0

        # Iterates to add up the price
        for isbn in cart_items:
            bookInfo = inventoryDatabase.getBookInfoByISBN(isbn)
            totalPrice += bookInfo['price']

        # No idea if this will exist just for concept
        inventoryDatabase.updateStock(cart_items)

        User.clearCart(userID)
        # prints checkout notifying user
        print(f"Checkout successful. Total Price: ${total_price:.2f}")


    def getCartItems(self, userID):
        # returns cart item info
        return User.getCartItems(userID)


    
