import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="pickles",
    db = "transit_system"
)

cursor = database.cursor()


def read_data():
    select_query = "SELECT Bus_Type FROM bus"
    cursor.execute(select_query)
    
    # Fetch all the data returned by the database
    bus_types = cursor.fetchall()
    
    # Print all the data returned by the database
    for bus_type in bus_types:
        print(bus_type)

read_data()