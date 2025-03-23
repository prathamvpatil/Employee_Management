import mysql.connector

connection = mysql.connector.connect(
    host="localhost", user="root", password="Pratham@123", database="employee"
)

#check employee function
def check_employee(employee_id):
    # To select all the employees with matching id from database
    sql = 'SELECT * FROM employees WHERE employee_id = %s'

    # Making cursor buffered so that rowcount method work properly
    cursor = connection.cursor(buffered=True)
    data = (employee_id,)

    #Execute the query
    cursor.execute(sql, data)

    # Fetch the first row to check if employee exists
    employee = cursor.fetchone();
    # close the cursor
    cursor.close()
    # Return True if employee exists else False
    return employee is not None

# Add employee function

def add_employee():
    Id = input("Please enter employee id: ")
    # Check for the employee is already existing or not.
    if check_employee(Id):
        print("Employee already exists. Please enter a new id.")
        return
    else:
        Name = input("Enter Employee Name: ")
        Post = input("Enter Employee Post: ")
        Salary = input("Enter Employee Salary: ")
        # Inserting the details into the table

        sqql = 'INSERT INTO employees (id, name, position, salary) VALUES (%s, %s, %s, %s)'
        data = (Id, Name, Post, Salary)
        cursor = connection.cursor()

        try:
            # Execute the query
            cursor.execute(sqql, data)

            # Commit the transaction
            connection.commit()
            print("Employee added successfully")
        
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            connection.rollback()
        
        finally:
            # Close the cursor
            cursor.close()