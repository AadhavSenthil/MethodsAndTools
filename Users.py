import sqlite3


class User:
    def __init__(self, databaseName, tableName):
        self.loggedIn = False
        self.userID = " "
        self.database = databaseName
        self.tableName = tableName


        
    def login(self):
        user = sqlite3.connect(self.database)
        cursor = user.cursor()

        self.userID = input("UserID:")
        password = input("Password:")
        cursor.execute(f'SELECT Users.Password, Users.UserID FROM {self.tableName} WHERE UserID=? AND Password=?', (self.userID,password))
        row = cursor.fetchone()
        if row:
            print("Login Success")
            self.loggedIn =True
            return True
        else:
            print("Login Failed")
            self.loggedIn = False
            return False

    def logout(self):
        if self.loggedIn == True:
            self.userID = " "
            self.loggedIn = False

        return False

    def viewAccountInformation(self):
        user = sqlite3.connect(self.database)
        cursor = user.cursor()
        if self.loggedIn == True:
            cursor.execute(f'SELECT * FROM {self.tableName} WHERE UserID=?', (self.userID,))
            row = cursor.fetchall()
            print("Account Info:")
            if not row:
                print("No matching User.")
            else:
                print(row)

        else:
            print("Please Login to see Account Information.")


    def createAccount(self):
        user = sqlite3.connect(self.database)
        cursor = user.cursor()
        while True:
            self.userID = input("UserID: ")
            email = input("Email: ")
            password = input("Password: ")
            firstName = input("First Name: ")
            lastName = input("Last Name: ")
            address = input("Address: ")
            city = input("City: ")
            state = input("State: ")
            zip = input("Zip: ")
            payment = input("Payment: ")
        #if(self.userID == cursor.execute(f"SELECT UserID FROM {self.tableName}")):
            #self.userID = input("Please input a valid UserID: ")           

            try:
                cursor.execute(f"INSERT INTO {self.tableName} (UserID, Email, Password, FirstName, LastName, Address, City, State, Zip, Payment) Values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (self.userID, email, password, firstName, lastName, address, city, state, zip, payment))

                user.commit()
                break

            except sqlite3.IntegrityError:
            # Handle the unique constraint violation
                self.userID = input("UserID already exists! Input another UserID: ")
    

    def getLoggedIn(self):
        return self.loggedIn

    def getUserID(self):
        return self.userID





