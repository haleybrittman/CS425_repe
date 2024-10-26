import mysql.connector

try:
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Hoplite1", # personal
        db = "transit_system"
    )
    database.autocommit=True
    
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
        table_dict = {
        '1': 'bus',
        '2': 'bus_bus_route',
        '3': 'bus_route',
        '4': 'bus_route_bus_stops',
        '5': 'bus_stops',
        '6': 'bus_stops_stop_order',
        '7': 'bus_stops_time',
        '8': 'line',
        '9': 'line_train_stops',
        '10': 'passenger',
        '11': 'train',
        '12': 'train_line',
        '13': 'train_stop',
        '14': 'train_stops_time'}
    
        while True:
            number = input('Which table would you like to use? Enter a number: ')
            if number in table_dict:
                return table_dict[number]
            else:
                print('Please select a valid number')
                
        


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

    def insert_data(table):
        return
    def update_data(table):
        column= input('Update which column? ')
        column_content= input('Set the column to what? ')
        row_change= input('Where... ')
        row_content=input('equals... ')
        update_query = f"UPDATE {table} SET {column} = {column_content} WHERE {row_change} = {row_content}"
        
        try:
            cursor.execute(update_query)
        except Exception as e:
            print('Error:', e)


    def delete_data(table):
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
                table = selectTable()
                insert_data(table)
            elif menuChoice == '3':
                table = selectTable()
                update_data(table)
            elif menuChoice == '4':
                table = selectTable()
                delete_data(table)
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