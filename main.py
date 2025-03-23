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
        sqql = 'DELETE FROM employees WHERE id = %s'
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
