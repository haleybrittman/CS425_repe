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
        cursor.execute("show full tables where Table_Type != 'VIEW'")
        tables = cursor.fetchall()
        print("\nAvailable tables:")
        for idx, table in enumerate(tables):
            print(f"{idx + 1}. {table[0]}")
        return

    def selectTable():
        while True:
            number = input('Which table would you like to use? Enter a number: ')
            if number == '1':
                table = 'bus'
                break
            elif number == '2':
                table = 'bus_bus_route'
                break
            elif number == '3':
                table = 'bus_route'
                break
            elif number == '4':
                table = 'bus_route_bus_stops'
                break
            elif number == '5':
                table = 'bus_stops'
                break
            elif number == '6':
                table = 'bus_stops_stop_order'
                break
            elif number == '7':
                table = 'bus_stops_time'
                break
            elif number == '8':
                table = 'line'
                break
            elif number == '9':
                table = 'line_train_stops'
                break
            elif number == '10':
                table = 'passenger'
                break
            elif number == '11':
                table = 'train'
                break
            elif number == '12':
                table = 'train_line'
                break
            elif number == '13':
                table = 'train_stop'
                break
            elif number == '14':
                table = 'train_stops_time'
                break
            else:
                print('Please select a valid number')
                
        return table


    def read_data(table):
        select_query = f"SELECT * FROM {table}"
        cursor.execute(select_query)
        
        # Fetch all the data returned by the database
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in  cursor.description]
        
        # Print all the data returned by the database
        print(column_names)
        for row in rows:
            print(row)
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
                showTables()
                table = selectTable()
                read_data(table)
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