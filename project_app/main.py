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


    def showTables(): # Displays tables excluding views
        cursor.execute("show full tables where Table_Type != 'VIEW'")
        tables = cursor.fetchall()
        print("\nAvailable tables:")
        for idx, table in enumerate(tables):
            print(f"{idx + 1}. {table[0]}")
        return

    def selectTable(): # Reused for options so user can select which table they're using for the option
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
    
        while True: # Error checking for invalid number
            number = input('Which table would you like to use? Enter a number: ')
            if number in table_dict:
                print('')
                return table_dict[number]
            else:
                print('Please select a valid number')
                
        


    def read_data(table): # Read function. Reads data
        select_query = f"SELECT * FROM {table}"
        cursor.execute(select_query)
        
        # Fetch all the data returned by the database
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in  cursor.description]
        
        # Print all the data returned by the database
        print(column_names)
        for row in rows:
            print(row)

    def insert_data(table): # Create function. Insertion of data
        table_dict={ # Error checking is handled by selectTable()
        'bus':'(bus_id,bus_type,Wheelchair_accessibility,Capacity)',
        'bus_bus_route':'(Bus_ID, Route_no)',
        'bus_route':'(route_no, name, direction)',
        'bus_route_bus_stops':'(Stop_name, Route_no)',
        'bus_stops':'(Stop_Name, Route, Stop_Order)',
        'bus_stops_stop_order':'(Stop_Name, Location, Route, Stop_Order)',
        'bus_stops_time':'(Stop_Name, Route, Time, ETA)',
        'line':'(ColorType, Name, Direction, Start)',
        'line_train_stops':'(ColorType, Name, Direction, Station_Name)',
        'passenger':'(Name, Passenger_ID, Disabled, Phone_Number, train_id, bus_id)',
        'train':'(Train_ID, Capacity)',
        'train_line':'(Train_ID, ColorType, Name, Direction)',
        'train_stop':'(Station_Name, ColorType, Name, Direction)',
        'train_stops_time':'(TID, Station_Name, ColorType, Line_Name, Direction, Time)'}
        values=input(f'Input values in the following format: {table_dict[table]}: ')
        insert_query = f"INSERT INTO {table} VALUES {values}"
        
        try:
            cursor.execute(insert_query)
        except Exception as e:
            print('Error:', e)


    def update_data(table): # Update function. Updates data in a row
        column= input('Update which column? ')
        column_content= input('Set the column to what? ')
        row_change= input('Where... ')
        row_content=input('equals... ')
        update_query = f"UPDATE {table} SET {column} = {column_content} WHERE {row_change} = {row_content}"
        
        try:
            cursor.execute(update_query)
        except Exception as e:
            print('Error:', e)

"""
    def delete_data(table):
            """Delete a row from a specified table based on user input."""
            row_delete = input('Delete from ' + table + ' where column name is: ')
            row_content = input('Value to delete for this column: ')
    
            # Parameterized delete query
            delete_query = f"DELETE FROM {table} WHERE {row_delete} = {row_content}"
            
            try:
                cursor.execute(delete_query, (row_content,))
                database.commit()  # Commit changes to finalize the deletion
                print(f"Deleted rows from {table} where {row_delete} = {row_content}")
            except Exception as e:
                print('Error:', e)
"""





    
    def delete_data(table): # Delete function. Delete a row
        row_delete= input('Delete from '+table+' where... ')
        row_content=input('equals... ')
        delete_query = f"DELETE FROM {table} WHERE {row_delete} = {row_content}"
        
        try:
            cursor.execute(delete_query)
        except Exception as e:
            print('Error:', e)

    
    def main(): # Main function. Displays menu until user exits
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
