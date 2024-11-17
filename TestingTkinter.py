import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Database connection (update with your credentials)
try:
    database = mysql.connector.connect(
        host='localhost',
        user='root',
        password='pickles',
        database='transit_system'
    )
    cursor = database.cursor()
except mysql.connector.Error as err:
    print("Database connection error:", err)
    exit()


def showTables():
    """Displays tables excluding views."""
    cursor.execute("SHOW FULL TABLES WHERE Table_Type != 'VIEW'")
    tables = cursor.fetchall()
    return tables


def read_data(table):
    """Read data from a table and return the rows and column names."""
    select_query = f"SELECT * FROM {table}"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
    return rows, column_names


def display_data(table):
    """Fetch data from the selected table and display it in the Treeview widget."""
    try:
        rows, columns = read_data(table)
        # Clear the existing Treeview
        for item in tree.get_children():
            tree.delete(item)
        
        # Update column headings dynamically
        tree["columns"] = columns
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=100)

        # Populate the Treeview with data
        for row in rows:
            tree.insert("", "end", values=row)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def selectTable():
    """Prompt user to select a table."""
    tables = showTables()
    table_dict = {str(i + 1): table[0] for i, table in enumerate(tables)}
    
    # Open a new window for table selection
    def on_select():
        selected = table_listbox.curselection()
        if selected:
            selected_table.set(table_dict[str(selected[0] + 1)])
            selection_window.destroy()
        else:
            messagebox.showwarning("Selection Error", "No table selected!")

    selection_window = tk.Toplevel(root)
    selection_window.title("Select Table")
    tk.Label(selection_window, text="Available Tables").pack(pady=5)
    table_listbox = tk.Listbox(selection_window)
    table_listbox.pack(pady=5)
    
    for idx, table in enumerate(table_dict.values(), start=1):
        table_listbox.insert(idx, table)

    tk.Button(selection_window, text="Select", command=on_select).pack(pady=5)

    selection_window.transient(root)
    selection_window.grab_set()
    root.wait_window(selection_window)
    return selected_table.get()


# Tkinter setup
root = tk.Tk()
root.title("Database Table Viewer")
selected_table = tk.StringVar(value="")

# Create Treeview for displaying records
tree = ttk.Treeview(root, show="headings")
tree.pack(pady=10, fill="both", expand=True)

# Add a scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# Add buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Show All Records button
tk.Button(button_frame, text="Show All Records", command=lambda: display_data(selected_table.get())).grid(row=0, column=0, padx=10)

# Select Table button
tk.Button(button_frame, text="Select Table", command=lambda: selected_table.set(selectTable())).grid(row=0, column=1, padx=10)

# Exit button
tk.Button(button_frame, text="Exit", command=root.destroy).grid(row=0, column=2, padx=10)

root.mainloop()