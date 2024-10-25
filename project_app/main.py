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




    def read_data():
        select_query = "SELECT Bus_Type FROM bus"
        cursor.execute(select_query)
        
        # Fetch all the data returned by the database
        bus_types = cursor.fetchall()
        
        # Print all the data returned by the database
        for bus_type in bus_types:
            print(bus_type)

    read_data()
except mysql.connector.Error as e:
    print("Error:", e)