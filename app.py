import streamlit as st
import subprocess
import sqlite3


def sum_numbers():
    # Connect to the database
    conn = sqlite3.connect('numbers.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a SELECT statement to get the sum of column a and b
    cursor.execute('SELECT SUM(a + b) FROM numbers')

    # Fetch the result of the query
    result = cursor.fetchone()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Return the result
    return result[0]


def page1():
    st.title("Page 1")
    st.write("Welcome to Page 1!")
    # Add widgets and functionality for page 1 here

    def create_file():
        ssh_cmd = 'ssh -i C:\\Users\\reyne\\Downloads\\test2thesis.pem azureuser@20.251.115.193 \'echo "This is a sample text file" > ~/sample.txt\''
        subprocess.Popen(["powershell.exe", "-Command", ssh_cmd])

    # Streamlit code to create a button that executes the create_file() function when clicked
    if st.button("Create File"):
        create_file()

    # Define the function for the first page

    # Add widgets and functionality for page 2 here


# Define the function for the second page

def page2():
    st.title("Page 2")
    st.write("Welcome to Page 2!")

    def sum_numbers():
        # Define the SSH command to execute
        ssh_cmd = 'ssh -i C:\\Users\\reyne\\Downloads\\test2thesis.pem azureuser@20.251.115.193 "sqlite3 test.db \'SELECT SUM(a + b) FROM numbers;\'"'

        # Execute the command and capture the output
        proc = subprocess.Popen(
            ["powershell.exe", "-Command", ssh_cmd], stdout=subprocess.PIPE)
        output, error = proc.communicate()

        # Decode the output and extract the result
        result = output.decode().strip()

        # Return the result
        return result

    # Streamlit code to create a button that executes the create_file() function when clicked
    if st.button("Sum columns in SQLite3"):
        # Create a Streamlit app
        st.title('Sum of Numbers')
        result = sum_numbers()
        st.write('The sum of numbers in the database is:', result)


# Define the page selection menu
menu = ["Page 1", "Page 2"]
choice = st.sidebar.selectbox("Select a page", menu)

# Show the appropriate page based on the user's selection
if choice == "Page 1":
    page1()
else:
    page2()
