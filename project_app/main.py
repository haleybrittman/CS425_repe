import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import mysql.connector


class TransitSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Transit System Database")
        self.database = None

        # Connect to the database
        try:
            password = simpledialog.askstring("Database Connection", "Enter your database password:", show='*')
            self.database = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd=password,
                db="transit_system"
            )
            self.database.autocommit = True

            if self.database.is_connected():
                messagebox.showinfo("Connection", "Connected to Transit System Database Successfully")
                self.cursor = self.database.cursor()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", str(err))
            raise SystemExit("Database connection failed.")

        # Create the GUI
        self.create_gui()

    def create_gui(self):
        # Menu Options
        menu_frame = ttk.LabelFrame(self.root, text="Options")
        menu_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        ttk.Button(menu_frame, text="Show Tables", command=self.showTables).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(menu_frame, text="Read Data", command=self.read_data).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(menu_frame, text="Insert Data", command=self.insert_data).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(menu_frame, text="Update Data", command=self.update_data).grid(row=0, column=3, padx=5, pady=5)
        ttk.Button(menu_frame, text="Delete Data", command=self.delete_data).grid(row=0, column=4, padx=5, pady=5)
        ttk.Button(menu_frame, text="Special Queries", command=self.advanced_queries).grid(row=0, column=5, padx=5, pady=5)

        # Output Textbox
        self.textbox = tk.Text(self.root, wrap="word", height=20, width=80)
        self.textbox.grid(row=1, column=0, padx=10, pady=10)

    def showTables(self): # Displays tables excluding views
        try:
            self.cursor.execute("SHOW FULL TABLES WHERE Table_Type != 'VIEW'")
            tables = self.cursor.fetchall()
            self.textbox.config(state='normal')
            self.textbox.delete(1.0, tk.END)
            self.textbox.insert(tk.END, "Available Tables:\n")
            for idx, table in enumerate(tables):
                self.textbox.insert(tk.END, f"{idx + 1}. {table[0]}\n")
            self.textbox.config(state='disabled')
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def selectTable(self): # Reused for options so user can select which table they're using for the option
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
            '14': 'train_stops_time'
        }
        choice = simpledialog.askstring("Select Table", "Choose a table number:\n" + "\n".join(
            [f"{key}. {value}" for key, value in table_dict.items()]))

        if choice in table_dict:  # Error checking for valid number
            return table_dict[choice]

        # Invalid number
        messagebox.showerror("Invalid Selection", "Please select a valid number.")


    def read_data(self): # Read function. Reads data
        table = self.selectTable()
        if not table:
            return

        try:
            self.cursor.execute(f"SELECT * FROM {table}")
            rows = self.cursor.fetchall() # Fetch all the data returned by the database
            column_names = [desc[0] for desc in self.cursor.description]
            self.textbox.config(state='normal')
            self.textbox.delete(1.0, tk.END)
            self.textbox.insert(tk.END, f"Data from {table}:\n")
            self.textbox.insert(tk.END, f"{column_names}\n")
            for row in rows: # Insert data into textbox
                self.textbox.insert(tk.END, f"{row}\n")
            self.textbox.config(state='disabled')
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def insert_data(self): # Create function. Insertion of data
        table = self.selectTable() # Error checking is handled by selectTable()
        if not table:
            return

        values = simpledialog.askstring("Insert Data", f"Input values for {table}:")
        if not values:
            messagebox.showerror("Invalid Selection", "Please provide valid input.")
            return

        insert_query = f"INSERT INTO {table} VALUES ({values})"
        try:
            self.textbox.config(state='normal')
            self.cursor.execute(insert_query)
            self.textbox.config(state='disabled')
            messagebox.showinfo("Success", "Data inserted successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_data(self): # Update function. Updates data in a row
        table = self.selectTable()
        if not table:
            return

        column = simpledialog.askstring("Update Data", "Update which column?")
        column_content = simpledialog.askstring("Update Data", "Set the column to what?")
        row_change = simpledialog.askstring("Update Data", "Where column:")
        row_content = simpledialog.askstring("Update Data", "Equals:")

        update_query = f"UPDATE {table} SET {column} = %s WHERE {row_change} = %s"
        try:
            self.cursor.execute(update_query, (column_content, row_content))
            messagebox.showinfo("Success", f"Updated {column} in {table}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_data(self): # Delete a row from a specified table based on user input.
        table = self.selectTable()
        if not table:
            return

        row_delete = simpledialog.askstring("Delete Data", f"Delete from {table} where column:")
        row_content = simpledialog.askstring("Delete Data", "Value:")

        delete_query = f"DELETE FROM {table} WHERE {row_delete} = %s"
        try:
            self.cursor.execute(delete_query, (row_content,))
            messagebox.showinfo("Success", "Data deleted successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def advanced_queries(self):
        queries = {
            "Find buses and trains that have the same capacity": """
            SELECT 'Bus' AS Vehicle_Type, Bus_ID AS Vehicle_ID, Capacity
            FROM Bus
            WHERE Capacity IN (SELECT Capacity FROM Train)
            UNION
            SELECT 'Train' AS Vehicle_Type, Train_ID AS Vehicle_ID, Capacity
            FROM Train
            WHERE Capacity IN (SELECT Capacity FROM Bus);
            """,

            "List the names and IDs of passengers who rode both a bus and a train.": """
            SELECT Name, Passenger_ID
            FROM Passenger
            WHERE Bus_ID IS NOT NULL AND Train_ID IS NOT NULL;
            """,

            "Shows the ID and capacity of buses that have a larger capacity than the biggest train.": """
            SELECT Bus_ID, Capacity
            FROM Bus
            WHERE Capacity > (SELECT MAX(Capacity) FROM Train);
            """,

            "Find the most frequent stop for each bus route.": """
            WITH StopFrequency AS (
            SELECT Stop_Name, Route, COUNT(*) AS Frequency
            FROM Bus_Stops_Stop_Order
            GROUP BY Stop_Name, Route
            )
            SELECT Route, Stop_Name, MAX(Frequency) AS MaxFrequency
            FROM StopFrequency
            GROUP BY Route;
            """,

            "Calculate the average, minimum, and maximum capacity of all trains.": """
            SELECT
            AVG(Capacity) AS AvgCapacity,
            MIN(Capacity) AS MinCapacity,
            MAX(Capacity) AS MaxCapacity
            FROM Train;
            """,

            "Count the number of passengers for each bus route.": """
            SELECT
            BR.route_no,
            COUNT(P.Passenger_ID) AS TotalPassengers,
            SUM(COUNT(P.Passenger_ID)) OVER (ORDER BY BR.route_no) AS CumulativePassengers
            FROM Bus_Route BR
            LEFT JOIN Bus_Bus_Route BBR ON BR.route_no = BBR.Route_no
            LEFT JOIN Passenger P ON BBR.Bus_ID = P.Bus_ID
            GROUP BY BR.route_no
            ORDER BY BR.route_no;
            """,

            "List all Teal line trains going East.": """
            SELECT Train_ID, ColorType, Station_Name, Time
            FROM TrainView
            WHERE ColorType = 'Teal' AND Direction = 'East'
            ORDER BY Time;
            """,

            "Update bus capacity": """
            CALL update_bus_capacity(1, 35);
            """,

            "Show train lines that have more than 3 distinct stations.": """
            SELECT ColorType, Name, Direction, COUNT(DISTINCT Station_Name) AS StationCount
            FROM Line_Train_Stops
            GROUP BY ColorType, Name, Direction
            HAVING COUNT(DISTINCT Station_Name) > 3;
            """,

            "Find train lines that don't have any stops.": """
            SELECT ColorType, Name, Direction
            FROM Line
            WHERE NOT EXISTS (
            SELECT 1
            FROM Line_Train_Stops
            WHERE Line.ColorType = Line_Train_Stops.ColorType
            AND Line.Name = Line_Train_Stops.Name
            AND Line.Direction = Line_Train_Stops.Direction
            );
            """
        }
        special_pane = tk.Toplevel(self.root)
        special_pane.title("Advanced Queries")
        special_pane.geometry("500x400")
        
        # Create a listbox to display queries
        listbox = tk.Listbox(special_pane, height=20, width=70)
        listbox.pack(padx=10, pady=10)

        # Populate the listbox with query names
        for query_name in queries.keys():
            listbox.insert(tk.END, query_name)

        def execute_query():
            # Get the selected query
            selected_index = listbox.curselection()
            if not selected_index:
                messagebox.showwarning("No Selection", "Please select a query to execute.")
                return

            query_name = listbox.get(selected_index)
            query = queries[query_name]

            try:
                # Execute the query
                self.cursor.execute(query)
                rows = self.cursor.fetchall()
                column_names = [desc[0] for desc in self.cursor.description]

                # Display results in the main textbox
                self.textbox.config(state='normal')
                self.textbox.delete(1.0, tk.END)
                self.textbox.insert(tk.END, f"Results for: {query_name}\n")
                self.textbox.insert(tk.END, f"{column_names}\n")
                for row in rows:
                    self.textbox.insert(tk.END, f"{row}\n")
                self.textbox.config(state='disabled')
                special_pane.destroy()
            except Exception as e:
                messagebox.showerror("Query Error", str(e))
        

        # Button to execute the selected query
        execute_button = ttk.Button(special_pane, text="Execute Query", command=execute_query)
        execute_button.pack(pady=10)

        # Prevent other pane interaction
        special_pane.grab_set() 
        special_pane.wait_window(special_pane)
        





    def on_closing(self): # handle closing of GUI 
        if self.database and self.database.is_connected():
            self.cursor.close()
            self.database.close() # Close DB connection
            print("Database connection closed")
        self.root.destroy() # Remove GUI


if __name__ == "__main__": 
    root = tk.Tk()
    app = TransitSystem(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
