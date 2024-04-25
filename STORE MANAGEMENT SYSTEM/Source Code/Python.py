import mysql.connector as sql

conn = sql.connect(host='localhost', user='root', passwd='Hello12345', database='store')
if conn.is_connected():
    print('Successfully connected')
c = conn.cursor()

def register_user():
    print('User Registration')
    new_user = input('Enter a new Username: ')
    new_password = input('Enter a new Password: ')
    
    
    print('User registered successfully!')

def login():
    user_name = input('Enter your Username: ')
    password = input('Enter your Password: ')
    login_successful = True
    
    if login_successful:
        print('Connected successfully')
        while True:
            print('*' * 140)
            print('Convenience store'.center(140))
            print('1. Customer details'.center(140))
            print('2. Product details'.center(140))
            print('3. Worker details'.center(140))
            print('4. Exit'.center(140))
            print('*' * 140)
            choice = int(input('Enter the Choice: '))
            
            if choice == 1:
                print('*' * 140)
                print('1. Add customer details'.center(140))
                print('2. Delete customer details'.center(140))
                print('3. Display specific customer record'.center(140))
                print('4. Display all customer records'.center(140))
                print('*' * 140)
                sub_choice = int(input('Enter your choice: '))
                
                if sub_choice == 1:
                    cust_name = input('Enter your Name: ')
                    phone_no = int(input('Enter your Phone Number: '))
                    cost = float(input('Enter your Cost: '))
                    sql_insert = "INSERT INTO customer_details VALUES (%s, %s, %s)"
                    values = (phone_no, cust_name, cost)
                    c.execute(sql_insert, values)
                    conn.commit()
                    print('Data is updated')
                
                elif sub_choice == 2:
                    phone_no = int(input('Enter the Phone Number to delete: '))
                    sql_delete = "DELETE FROM customer_details WHERE phone_no = %s"
                    values = (phone_no,)
                    c.execute(sql_delete, values)
                    conn.commit()
                    print('Data is deleted')
                
                elif sub_choice == 3:
                    phone_no = int(input('Enter the Phone Number to display: '))
                    sql_select = "SELECT * FROM customer_details WHERE phone_no = %s"
                    values = (phone_no,)
                    c.execute(sql_select, values)
                    records = c.fetchall()
                    for record in records:
                        print(record)
                
                elif sub_choice == 4:
                    c.execute('SELECT * FROM customer_details')
                    records = c.fetchall()
                    for record in records:
                        print(record)
            
            elif choice == 2:
                print('*' * 140)
                print('1. Add product details'.center(140))
                print('2. Delete product details'.center(140))
                print('3. Display specific product record'.center(140))
                print('4. Display all product records'.center(140))
                print('*' * 140)
                sub_choice = int(input('Enter your choice: '))
                
                if sub_choice == 1:
                    product_name = input('Enter Product Name: ')
                    product_cost = float(input('Enter the Cost: '))
                    sql_insert = "INSERT INTO product_details VALUES (%s, %s)"
                    values = (product_name, product_cost)
                    c.execute(sql_insert, values)
                    conn.commit()
                    print('Data is updated')
                
                elif sub_choice == 2:
                    product_name = input('Enter the Product Name to delete: ')
                    sql_delete = "DELETE FROM product_details WHERE product_name = %s"
                    values = (product_name,)
                    c.execute(sql_delete, values)
                    conn.commit()
                    print('Data is deleted')
                
                elif sub_choice == 3:
                    product_name = input('Enter the Product Name to display: ')
                    sql_select = "SELECT * FROM product_details WHERE product_name = %s"
                    values = (product_name,)
                    c.execute(sql_select, values)
                    records = c.fetchall()
                    for record in records:
                        print(record)
                
                elif sub_choice == 4:
                    c.execute('SELECT * FROM product_details')
                    records = c.fetchall()
                    for record in records:
                        print(record)
            
            elif choice == 3:
                print('*' * 140)
                print('1. Add worker details'.center(140))
                print('2. Delete worker details'.center(140))
                print('3. Display specific worker record'.center(140))
                print('4. Display all worker records'.center(140))
                print('*' * 140)
                sub_choice = int(input('Enter your choice: '))
                
                if sub_choice == 1:
                    worker_name = input('Enter the Name: ')
                    worker_work = input('Enter the Work: ')
                    worker_age = int(input('Enter the Age: '))
                    worker_salary = float(input('Enter the Salary: '))
                    phone_no = int(input('Enter the Phone Number: '))
                    sql_insert = "INSERT INTO worker_details VALUES (%s, %s, %s, %s, %s)"
                    values = (worker_name, worker_work, worker_age, worker_salary, phone_no)
                    c.execute(sql_insert, values)
                    conn.commit()
                    print('Data is updated')
                
                elif sub_choice == 2:
                    phone_no = int(input('Enter the Phone Number to delete: '))
                    sql_delete = "DELETE FROM worker_details WHERE phone_no = %s"
                    values = (phone_no,)
                    c.execute(sql_delete, values)
                    conn.commit()
                    print('Data is deleted')
                
                elif sub_choice == 3:
                    phone_no = int(input('Enter the Phone Number to display: '))
                    sql_select = "SELECT * FROM worker_details WHERE phone_no = %s"
                    values = (phone_no,)
                    c.execute(sql_select, values)
                    records = c.fetchall()
                    for record in records:
                        print(record)
                
                elif sub_choice == 4:
                    c.execute('SELECT * FROM worker_details')
                    records = c.fetchall()
                    for record in records:
                        print(record)
            
            elif choice == 4:
                print('Exiting...')
                break

print('Store Management System')
while True:
    print('*' * 140)
    print('1. Login'.center(140))
    print('2. Register'.center(140))
    print('3. Exit'.center(140))
    print('*' * 140)
    choice = int(input('Enter your Choice: '))
    
    if choice == 1:
        login()
    
    elif choice == 2:
        register_user()
    
    elif choice == 3:
        print('Exiting...')
        break
