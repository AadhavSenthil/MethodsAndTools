import sqlite3

class Inventory:
    def __init__(self, databaseName, tableName):
        self.databaseName = databaseName
        self.tableName = tableName

    def Inventory(self):
        # Establish connection
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        # Create table if it doesn't exist
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {self.tableName} (
            "Title" TEXT NOT NULL,
            "ISBN" INTEGER NOT NULL UNIQUE,
            "Stock" INTEGER NOT NULL,
            "Pages" INTEGER NOT NULL,
            "Genre" TEXT NOT NULL,
            "ReleaseDate" TEXT NOT NULL,
            PRIMARY KEY("ISBN")
        )""")

    def view_inventory(self):
        # Establish connection
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        # Select everything from table
        cursor.execute(f"SELECT * FROM {self.tableName}")
        # Fetches all the rows
        rows = cursor.fetchall()
        print("Inventory: ")
        # If inventory empty
        if not rows:
            print("Empty")
        else:
            for row in rows:
                print(row)

    def search_inventory(self):
        title = input("Please enter a book to search: ")
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        # Comma after title used to read as tuple
        cursor.execute(f"SELECT * FROM {self.tableName} WHERE Title = ?", (title,))
        rows = cursor.fetchall()
        if not rows:
            print("No matching books found.")
        else:
            print("Matching books: ")
            for row in rows:
                print(row)
    
    def decreaseStock(self, ISBN):
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        cursor.execute(f"UPDATE INVENTORY SET Stock=Stock-1 WHERE ISBN={ISBN} ")
        connection.commit()
    
    def getDatabase(self):
        return self.databaseName

# Create an instance of the Inventory class using the __init__ method
inventory_instance = Inventory("inventory.db", "Inventory")




