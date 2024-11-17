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


    def read_data(self):
        table = self.selectTable()
        if not table:
            return

        try:
            self.cursor.execute(f"SELECT * FROM {table}")
            rows = self.cursor.fetchall()
            column_names = [desc[0] for desc in self.cursor.description]
            self.textbox.config(state='normal')
            self.textbox.delete(1.0, tk.END)
            self.textbox.insert(tk.END, f"Data from {table}:\n")
            self.textbox.insert(tk.END, f"{column_names}\n")
            for row in rows:
                self.textbox.insert(tk.END, f"{row}\n")
            self.textbox.config(state='disabled')
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def insert_data(self):
        table = self.selectTable()
        if not table:
            return

        values = simpledialog.askstring("Insert Data", f"Input values for {table}:")
        if not values:
            return

        insert_query = f"INSERT INTO {table} VALUES ({values})"
        try:
            self.textbox.config(state='normal')
            self.cursor.execute(insert_query)
            self.textbox.config(state='disabled')
            messagebox.showinfo("Success", "Data inserted successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_data(self):
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

    def delete_data(self):
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

    def on_closing(self):
        if self.database and self.database.is_connected():
            self.cursor.close()
            self.database.close()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TransitSystem(root)
    root.mainloop()
