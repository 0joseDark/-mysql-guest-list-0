import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Instructions for installing the required modules:
# 1. Install Python on Windows 10 from the official website: https://www.python.org
# 2. Ensure that MySQL is installed and configured on your system.
# 3. Install the necessary modules using the following commands in the terminal:
#    pip install mysql-connector-python

# MySQL database configuration
def configure_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"  # Replace with your password
        )
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS guests_db")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS guests_db.guests (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                password VARCHAR(255),
                email VARCHAR(255),
                phone VARCHAR(15)
            )
        """)
        connection.commit()
        connection.close()
    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", f"Error: {str(e)}")

# Function to add a guest
def add_guest():
    name = entry_name.get()
    password = entry_password.get()
    email = entry_email.get()
    phone = entry_phone.get()
    
    if not name or not password or not email or not phone:
        messagebox.showwarning("Empty Fields", "All fields are required!")
        return

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",  # Replace with your password
            database="guests_db"
        )
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO guests (name, password, email, phone)
            VALUES (%s, %s, %s, %s)
        """, (name, password, email, phone))
        connection.commit()
        connection.close()
        list_guests()
        clear_fields()
        messagebox.showinfo("Success", "Guest added successfully!")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error adding guest: {str(e)}")

# Function to remove a guest
def remove_guest():
    selected = guest_list.curselection()
    if not selected:
        messagebox.showwarning("None Selected", "Select a guest to remove.")
        return

    try:
        guest = guest_list.get(selected)
        guest_id = guest.split(" - ")[0]  # Assuming the ID is the first part
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",  # Replace with your password
            database="guests_db"
        )
        cursor = connection.cursor()
        cursor.execute("DELETE FROM guests WHERE id = %s", (guest_id,))
        connection.commit()
        connection.close()
        list_guests()
        messagebox.showinfo("Success", "Guest removed successfully!")
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error removing guest: {str(e)}")

# Function to list the guests
def list_guests():
    guest_list.delete(0, tk.END)
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",  # Replace with your password
            database="guests_db"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT id, name, email FROM guests")
        for guest in cursor.fetchall():
            guest_list.insert(tk.END, f"{guest[0]} - {guest[1]} ({guest[2]})")
        connection.close()
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error listing guests: {str(e)}")

# Function to clear the input fields
def clear_fields():
    entry_name.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

# GUI configuration
configure_database()
window = tk.Tk()
window.title("Guest List")
window.geometry("600x400")

# Labels and input fields
tk.Label(window, text="Name:").pack()
entry_name = tk.Entry(window)
entry_name.pack()

tk.Label(window, text="Password:").pack()
entry_password = tk.Entry(window, show="*")
entry_password.pack()

tk.Label(window, text="Email:").pack()
entry_email = tk.Entry(window)
entry_email.pack()

tk.Label(window, text="Phone:").pack()
entry_phone = tk.Entry(window)
entry_phone.pack()

# Buttons
tk.Button(window, text="Add", command=add_guest).pack(pady=5)
tk.Button(window, text="Remove", command=remove_guest).pack(pady=5)

# Guest list
guest_list = tk.Listbox(window, width=50, height=10)
guest_list.pack()

# Initialize the guest list
list_guests()

# Start the application
window.mainloop()
