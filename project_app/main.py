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
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        print("\nAvailable tables:")
        for idx, table in enumerate(tables):
            print(f"{idx + 1}. {table[0]}")
        return


    def read_data(table):
        select_query = "SELECT * FROM {table}"
        cursor.execute(select_query)
        
        # Fetch all the data returned by the database
        bus_types = cursor.fetchall()
        
        # Print all the data returned by the database
        for bus_type in bus_types:
            print(bus_type)
    def insert_data():
        return
    def update_data():
        return
    def delete_data():
        return

    def main():
        while True:
            print('\nMenu\n1. Read a table\'s data')
            print('2. Insert data into a table\n3. Update data in a table\n4. Delete data')
            print('5. Show all tables\n6. Exit')

            menuChoice = input('What would you like to do? ')
            if menuChoice == '1':
                read_data()
            elif menuChoice == '2':
                insert_data()
            elif menuChoice == '3':
                update_data()
            elif menuChoice == '4':
                delete_data()
            elif menuChoice == '5':
                showTables()
            elif menuChoice == '6':
                break
            else:
                print('Please choose a valid option')
            
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