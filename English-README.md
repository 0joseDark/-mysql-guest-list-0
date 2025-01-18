Here is the translated version of the file into English:

---

### Guide to Setting Up the Environment and Running the Script

Here is a detailed guide to set up the environment on Windows 10 and run the guest management script:

---

#### 1. **Install Python**
   - Download Python from the official website: [python.org/downloads](https://www.python.org/downloads/).
   - During installation, **check the "Add Python to PATH" option** to make Python accessible from the terminal.
   - Verify the installation by opening the terminal (or `cmd`) and typing:
     ```bash
     python --version
     ```

---

#### 2. **Install MySQL**
   - Download and install MySQL Community Server from the official website: [dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/).
   - During installation:
     1. Set a password for the `root` user (note this password, as it will be used in the script).
     2. Choose the default configuration to enable MySQL as a Windows service.
   - After installation, open **MySQL Workbench** (if included) or connect to MySQL via the terminal using:
     ```bash
     mysql -u root -p
     ```
   - Enter the password you set.

---

#### 3. **Install Required Modules**
   - Open the terminal or `cmd` and install the `mysql-connector-python` module using the command:
     ```bash
     pip install mysql-connector-python
     ```

---

#### 4. **Configure the Database**
   - The script automatically creates the necessary database and table. Ensure that the MySQL credentials in the script (host, user, password) are correct:
     ```python
     connection = mysql.connector.connect(
         host="localhost",
         user="root",
         password="your_password"  # Replace 'your_password' with the MySQL password
     )
     ```
   - If needed, you can test the MySQL connection before running the script:
     ```python
     import mysql.connector

     try:
         connection = mysql.connector.connect(
             host="localhost",
             user="root",
             password="your_password"
         )
         print("Connection successful!")
         connection.close()
     except mysql.connector.Error as err:
         print(f"Error: {err}")
     ```

---

#### 5. **Run the Script**
   - Save the Python script in a file with a `.py` extension (e.g., `guest_management.py`).
   - Run the script in the terminal by typing:
     ```bash
     python guest_management.py
     ```
   - The application window will open with fields and buttons to manage guests.

---

#### 6. **Use the Application**
   - **Add Guests**:
     1. Fill in the fields for `Name`, `Password`, `Email`, and `Phone`.
     2. Click the "Add" button.
   - **List Guests**:
     - Added guests will appear in the list automatically.
   - **Remove Guests**:
     1. Select a guest from the list.
     2. Click the "Remove" button.

---

#### 7. **Common Errors and Solutions**
   - **MySQL Connection Error**:
     - Check if the MySQL service is running on Windows. You can start the service manually:
       ```bash
       net start MySQL
       ```
   - **"ModuleNotFoundError" Error**:
     - Ensure the `mysql-connector-python` module is correctly installed:
       ```bash
       pip install mysql-connector-python
       ```
   - **Invalid Credentials**:
     - Confirm that the user, password, and host in the script match the MySQL configuration.

---

### Extras
- **Change the Window Title**:
  - Modify the text in the line:
    ```python
    window.title("Guest List")
    ```

- **Use Additional Fields in MySQL**:
  - To add new fields, update the MySQL table and the script. For example, to add a birthdate:
    ```sql
    ALTER TABLE guests ADD birth_date DATE;
    ```

---