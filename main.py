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