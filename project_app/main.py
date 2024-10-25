import mysql.connector

try:
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Hoplite1", # personal
        db = "transit_system"
    )
    if database.is_connected():
        print("Connected to Transit System Database Successfully")
    cursor = database.cursor()


    def showTables():
        query= "SHOW TABLES"

    def read_data():
        select_query = "SELECT Bus_Type FROM bus"
        cursor.execute(select_query)
        
        # Fetch all the data returned by the database
        bus_types = cursor.fetchall()
        
        # Print all the data returned by the database
        for bus_type in bus_types:
            print(bus_type)

    def main():
        while True:
            print('Menu\n1. Read a table\'s data')
            print('2. Insert data into a table\n3. Update data in a table\n4. Delete data')
            print('5. Show all tables\n6. Exit')

            menuChoice = input('What would you like to do?')
            if menuChoice == 1:
                read_data()
    if __name__ == "__main__":
        main()
except mysql.connector.Error as e:
    print("Error:", e)



finally:
    # Close DB connection
    if database.is_connected():
        cursor.close()
        database.close()
        print("Closed connection to Transit System Database.")