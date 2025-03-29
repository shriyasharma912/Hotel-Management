host='localhost',
user='root',
password='shriya2006',
database='hotel_management'
import mysql.connector
def establish_mysql_connection(host, user, password, database):
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='shriya2006',
            database='hotel_management'
        )
        print("MySQL connection established successfully.")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def close_mysql_connection(connection):
    # Close the connection
    if connection:
        connection.close()
        print("MySQL connection closed.")






import mysql.connector

# Establish a connection to the MySQL server
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="shriya2006",
    database="hotel_management"
)

# Create a cursor to interact with the database
cursor = connection.cursor()






# Function to add a new guest
def add_guest():
    name = input("Enter guest name: ")
    guest_id= input("Enter guests ID")
    room_number = input("Enter room number: ")
    check_in_date = input("Enter check-in date (YYYY-MM-DD): ")

    # Insert data into the 'guests' table
    insert_query = "INSERT INTO guests (name, guest_id, room_number, check_in_date) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, (name, guest_id, room_number, check_in_date))
    connection.commit()

    print("Guest record added.")


# Function to check out a guest
def check_out_guest():
    guest_id = input("Enter guest ID to check out: ")

    # Delete data from the 'guests' table
    delete_query = "DELETE FROM guests WHERE guest_id = %s"
    cursor.execute(delete_query, (guest_id,))
    connection.commit()

    print(f"Guest with ID {guest_id} has been checked out.")


# Function to add a new staff member
def add_staff():
    name = input("Enter staff name: ")
    staff_id= input("Enter staff ID")
    position = input("Enter staff position: ")

    # Insert data into the 'staff' table
    insert_query = "INSERT INTO staff (name, staff_id, position) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (name, staff_id, position))
    connection.commit()

    print("Staff record added.")



#Function to remove a staff member
def remove_staffdata():
    staff_id=input("Enter staff ID")

    # Insert data into the 'staff' table
    delete_query = "DELETE FROM staff WHERE staff_id = %s"
    cursor.execute(delete_query, (staff_id,))
    connection.commit()

    print(f"staff with ID {staff_id} has been checked out.")



# Select all data from the 'guests' table
def showallguestsdata():
    select_query = "SELECT * FROM guests"
    cursor.execute(select_query)
    # Fetch all rows
    all_guests = cursor.fetchall()
    # Print the data
    for guest in all_guests:
        print("Guest ID:", guest[0])
        print("Name:", guest[1])
        print("Room Number:", guest[2])
        print("Check-In Date:", guest[3])
        print("---")






def showallstaffsdata():
    select_query = "SELECT * FROM staff"
    cursor.execute(select_query)
    # Fetch all rows
    all_staffs = cursor.fetchall()
    # Print the data
    for staff in all_staffs:
        print("Staff ID:", staff[0])
        print("Name:", staff[1])
        print("Position:", staff[2])
        




def calculate_room_rent():
    room_type = input("Enter room type (single/double/suite): ").lower()
    duration = int(input("Enter duration of stay (in nights): "))
    additional_services = float(input("Enter cost of additional services: "))
    discount = float(input("Enter discount percentage: "))
    
    # Define per-night rates for each room type
    room_rates = {
        'single':1500.0,
        'double':2200.0,
        'suite': 3000.0
    }

    # Check if the provided room type is valid
    if room_type not in room_rates:
        print("Invalid room type.")
        return None

    # Calculate base room rent
    base_rent = room_rates[room_type] * duration

    
    
    # Calculate total room rent after considering additional services and discount
    total_room_rent = base_rent + additional_services - (base_rent * discount / 100)
    

    if total_room_rent is not None:
        print(f"Total room rent for {room_type} room for {duration} nights with additional services and discount: ₨{total_room_rent:.2f}")


    


print("""⚙︎⚙︎⚙︎⚙︎⚙︎⚙︎⚙︎⚙︎⚙ HOTEL MANAGEMENT SYSTEM ⚙︎⚙︎⚙︎⚙︎⚙︎⚙︎⚙
⚙︎⚙︎⚙︎⚙︎⚙︎⚙︎⚙︎⚙︎⚙CROWN  PLAZA⚙︎⚙︎⚙︎⚙︎⚙︎⚙︎⚙︎⚙︎⚙""")

print("""
""")

establish_mysql_connection(host,user,password,database)
print("""
""")




# Main loop for managing hotel records
while True:
    print("\nOptions:")
    print("1. Add a guest")
    print("2. Check out a guest")
    print("3. Add a staff member")
    print("4. Remove staff data")
    print("5.Show all guest data")
    print("6.Show all staff data")
    print("7. Calculate Room Rent")
    print("8. Exit")
    choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")

    if choice == '1':
        add_guest()
    elif choice == '2':
        check_out_guest()
    elif choice == '3':
        add_staff()
    elif choice == '4':
        remove_staffdata()
    elif choice == '5':
        showallguestsdata()
    elif choice == '6':
        showallstaffsdata()
    elif choice == '7':
        calculate_room_rent()
    elif choice == '8':
        break
    else:
        print("Invalid choice. Please enter a valid option.")



# Close the cursor and connection
cursor.close()
connection.close()
