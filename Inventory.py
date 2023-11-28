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
        connection.commit()

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
    
    def decreaseStock(self, ISBN, quantity):
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        cursor.execute(f"UPDATE {self.tableName} SET Stock=Stock-? WHERE ISBN=?", (quantity, ISBN))
        connection.commit()
    
    def getDatabase(self):
        return self.databaseName
    
    def get_book_info_by_isbn(self, ISBN):
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {self.tableName} WHERE ISBN = ?", (ISBN,))
        book_info = cursor.fetchone()
        connection.close()

        if book_info:
            return {
                "Title": book_info[0],
                "ISBN": book_info[1],
                "Stock": book_info[2],
                "Pages": book_info[3],
                "Genre": book_info[4],
                "ReleaseDate": book_info[5],
                "Price": book_info[6], 
            }
        else:
            return None





