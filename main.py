import mysql.connector

connection = mysql.connector.connect(
    host="localhost", user="root", password="Pratham@123", database="employee"
)

#check employee function
def check_employee(id):
    # To select all the employees with matching id from database
    sql = 'SELECT * FROM employees WHERE id = %s'

    # Making cursor buffered so that rowcount method work properly
    cursor = connection.cursor(buffered=True)
    data = (id,)

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

        sql = 'INSERT INTO employees (id, name, post, salary) VALUES (%s, %s, %s, %s)'
        data = (Id, Name, Post, Salary)
        cursor = connection.cursor()

        try:
            # Execute the query
            cursor.execute(sql, data)

            # Commit the transaction
            connection.commit()
            print("Employee added successfully")
        
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            connection.rollback()
        
        finally:
            # Close the cursor
            cursor.close()

# Remove employee function
def remove_employee():
    Id = input("Enter the Id: ")

    # Check if employee exists
    if not check_employee(Id):
        print("Employee does not exist")
        return
    else:
        # Delete the employee from the table
        sql = 'DELETE FROM employees WHERE id = %s'
        data = (Id,)
        cursor = connection.cursor()

        try:
            # Execute the query
            cursor.execute(sql, data)
            # Commit transaction
            connection.commit()
            print("Employee removed successfully")

        except:
            print(f"Error: {err}")
            connection.rollback()

        finally:
            # Close the cursor
            cursor.close()

# Promote Employee Function
def promote_employee():
    Id = input("Enter the Id: ")

    # Check if employee exists
    if not check_employee(Id):
        print("Employee does not exist")
        return
    else:
        try:
            Amount = float(input("Enter increase in Salary:"))

            # Query to fetch employee salary with given id
            sql_select = 'SELECT salary FROM employees WHERE id = %s'
            data = (Id,)
            cursor = connection.cursor()

            # Executing the query
            cursor.execute(sql_select, data)

            # Fetch the salary of employee with given id
            current_salary = cursor.fetchone()[0]
            new_salary = current_salary + Amount

            # Query to update the salary of employee with given id
            sql_update = 'UPDATE employees SET salary = %s WHERE id = %s'
            data_update = (new_salary, Id)

            # Executing the sql query to update the salary
            cursor.execute(sql_update, data_update)

            # Committing the transaction
            connection.commit()
            print("Employee promoted successfully")

        except (ValueError, mysql.connector.Error) as e:
            print(f"Error: {e}")
            connection.rollback();
        finally:
            # Close the cursor
            cursor.close()

# Display employee function
def display_employee():
    try:
        # Query to select all employees
        sql = 'SELECT * FROM employees'
        cursor = connection.cursor()
        # Execute the query
        cursor.execute(sql)

        # Fecthing all details of all employees
        employees = cursor.fetchall()
        for employee in employees:
            print("Employee Id : ",employee[0])
            print("Employee Name : ", employee[1])
            print("Employee Post : ", employee[2])
            print("Employee Salary : ", employee[3])
            print("------------------------------------")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        #close the cursor
        cursor.close()  

# Menu Function
def menu():
    while True:
        print("\nWelcome to Employee Management Record")
        print("Press:")
        print("1 to Add Employee")
        print("2 to Remove Employee")
        print("3 to Promote Employee")
        print("4 to Display Employees")
        print("5 to Exit")
        
        # Taking choice from user
        ch = input("Enter your Choice: ")

        if ch == '1':
            add_employee()
        elif ch == '2':
            remove_employee()
        elif ch == '3':
            promote_employee()
        elif ch == '4':
            display_employee()
        elif ch == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid Choice! Please try again.")

# Main function
if __name__ == "__main__":
    menu()
            