import sqlite3 

connection = sqlite3.connect("mini_world.db")

def insert_into_product():
    product_id = int(input("Enter product id: "))
    wholesale_price = int(input("Enter wholesale price: "))
    retail_price = int(input("Enter retail price: "))
    stock = int(input("Enter stock: "))
    crsr = connection.cursor()
    s = "INSERT INTO product (product_id,retail_price,wholesale_price,stock,profit) VALUES ("
    s+= str(product_id) + ',' + str(retail_price) + ',' + str(wholesale_price) + ',' + str(stock) + ',' + str(retail_price-wholesale_price) + ')' +  ';'
    crsr.execute(s)
    connection.commit()

def insert_into_outlet():
    outlet_id = int(input("Enter outlet id: "))
    PIN = int(input("Enter PIN: "))
    state = input("Enter state: ")
    city = input("Enter city: ")
    address = input("Enter address: ")
    crsr = connection.cursor()
    s = "INSERT INTO outlet (outlet_id,PIN,state,city,address) VALUES ("
    s+= str(outlet_id) + ',' + str(PIN) + ',' + ('\'' + state + '\'') + ',' + ('\'' + city + '\'') + ',' + ('\''  + address  + '\'') +  ')' + ';' 
    crsr.execute(s)
    connection.commit()

def insert_into_outlet_contact():
    outlet_id = int(input("Enter outlet id: "))
    phone_number = input("Enter phone number: ")
    crsr = connection.cursor()
    s = "INSERT INTO outlet_contact (outlet_id,phone_number) VALUES ("
    s+= str(outlet_id) + ',' + ('\'' + phone_number + '\'') + ')' + ';'
    crsr.execute(s)
    connection.commit()

def insert_into_supplier():
    lable = input("Enter supplier name: ")
    address = input("Enter supplier city: ")
    crsr = connection.cursor()
    s = "INSERT INTO supplier (lable,address) VALUES ("
    s+= ('\'' + lable + '\'') + ',' + ('\'' + address + '\'') + ')' + ';'
    crsr.execute(s)
    connection.commit()

def insert_into_supplier_contact():
    lable = input("Enter supplier name: ")
    phone_number = input("Enter phone number: ")
    crsr = connection.cursor()
    s = "INSERT INTO supplier_contact (lable,phone_number) VALUES ("
    s+= ('\'' + lable + '\'') + ',' + ('\'' + phone_number + '\'') + ')' + ';'
    crsr.execute(s)
    connection.commit()

def insert_into_transport():
    name = input("Enter transporter name: ")
    quantity = int(input("Enter quantity: "))
    crsr = connection.cursor()
    s = "INSERT INTO transport (company,quantity) VALUES ("
    s+= ('\'' + name + '\'') + ',' + str(quantity) + ')' + ';'
    crsr.execute(s)
    connection.commit()

def insert_into_customer():
    customer_id = int(input("Enter customer id: "))
    name = input("Enter name: ")
    house = input("Enter house: ")
    street = input("Enter street: ")
    city = input("Enter city: ")
    state = input("Enter state: ")
    crsr = connection.cursor()
    s = "INSERT INTO customer (customer_id,name,house,street,city,state) VALUES ("
    s+= str(customer_id) + ',' + ('\'' + name + '\'') + ',' + ('\'' + house + '\'') + ',' + ('\'' + street + '\'') +  ',' +('\'' + city + '\'') + ',' + ('\'' + state + '\'')  + ')' + ';' 
    crsr.execute(s)
    connection.commit()

def insert_into_customer_contact():
    customer_id = int(input("Enter customer id: "))
    phone_number = input("Enter phone number: ")
    crsr = connection.cursor()
    s = "INSERT INTO customer_contact (customer_id,phone_number) VALUES ("
    s+= str(customer_id) + ',' + ('\'' + phone_number + '\'') + ')' + ';'
    crsr.execute(s)
    connection.commit()

def insert_into_employee():
    employee_id = int(input("Enter employee id: "))
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    address = input("Enter address: ")
    crsr = connection.cursor()
    s = "INSERT INTO employee (employee_id,name,age,address) VALUES ("
    s+= str(employee_id) + ',' + ('\'' + name + '\'')+ ',' + str(age) + ',' + ('\'' + address + '\'') +  ')' + ';'
    crsr.execute(s)
    connection.commit()

def insert_into_job():
    salary = int(input("Enter salaray: "))
    designation = input("Enter designation: ")
    capacity = int(input("Enter capacity: "))
    currently_working = int(input("Enter currently_working: "))
    crsr = connection.cursor()
    s = "INSERT INTO job (salary,designation,capacity,currently_working,vacancy) VALUES ("
    s+= str(salary) + ',' + ('\'' + designation + '\'') +  ',' + str(capacity) + ',' + str(currently_working) + ',' + str(capacity-currently_working)+')' + ';'
    crsr.execute(s)
    connection.commit()

def insert_into_ferry():
    product_id = int(input("Enter product id: "))
    outlet_id = int(input("Enter outlet id: "))
    supplier = input("Enter supplier name: ")
    transporter = input("Enter transporter name: ")
    crsr = connection.cursor()

    s = "INSERT INTO ferry (product_id,outlet_id,supplier,transport_company) VALUES ("
    s+= str(product_id) + ',' + str(outlet_id) + ',' + ('\'' + supplier + '\'') + ',' + ('\'' + transporter + '\'') + ')' + ';'
    crsr.execute(s)
    connection.commit()

def insert_into_billing():
    product_id = int(input("Enter product id: "))
    outlet_id = int(input("Enter outlet id: "))
    customer_id = int(input("Enter customer id: "))

    crsr = connection.cursor()

    s = "INSERT INTO billing (product_id,outlet_id,customer_id) VALUES ("
    s+= str(product_id) + ',' + str(outlet_id) + ',' + str(customer_id) + ')' + ';'
    crsr.execute(s)
    connection.commit()

def insert_into_worker():
    employee_id = int(input("Enter employee id: "))
    outlet_id = int(input("Enter outlet id: "))
    designation = input("Enter designation: ")

    crsr = connection.cursor()

    s = "INSERT INTO worker (employee_id,outlet_id,designation) VALUES ("
    s+= str(employee_id) + ',' + str(outlet_id) + ',' + ('\'' + designation + '\'') + ')' + ';'
    crsr.execute(s)
    connection.commit()

def update_product():
    product_id = int(input("Enter product id of product which you want to update :"))
    wholesale_price = int(input("Enter new wholesale price: "))
    retail_price = int(input("Enter new retail price: "))
    stock = int(input("Enter new stock: "))
    crsr = connection.cursor()
    s = "UPDATE product SET "
    s += "wholesale_price =" + str(wholesale_price) + ','
    s += "retail_price =" + str(retail_price) + ','
    s += "profit =" + str(retail_price-wholesale_price) + ','
    s += "stock =" + str(stock)
    s+= " WHERE product_id =" + str(product_id)
    crsr.execute(s)
    connection.commit()

def update_outlet():
    outlet_id = int(input("Enter outlet id of outlet which you want to update :"))
    PIN = int(input("Enter new PIN: "))
    state = input("Enter new state: ")
    city = input("Enter new city: ")
    address = input("Enter new address: ")
    crsr = connection.cursor()
    s = "UPDATE outlet SET "
    s += "PIN =" + str(PIN) + ','
    s += "state =" + '\'' + state + '\'' + ','
    s += "city =" + '\'' + city + '\'' + ','
    s += "address =" + '\'' + address + '\'' + ' '
    s+= " WHERE outlet_id =" + str(outlet_id)
    crsr.execute(s)
    connection.commit()

def update_outlet_contact():
    old_phone_number = input("Enter phone_number of outlet_contact which you want to update :")
    phone_number = input("Enter new phone number: ")
    crsr = connection.cursor()
    s = "UPDATE outlet_contact SET "
    s += "phone_number =" + '\'' + phone_number + '\''

    s+= " WHERE phone_number =" + '\'' + old_phone_number + '\''
    crsr.execute(s)
    connection.commit()

def update_supplier():
    supplier_name = input("Enter name of supplier which you want to update :")
    address = input("Enter new address: ")
    crsr = connection.cursor()
    s = "UPDATE supplier SET "
    s += "address =" + '\'' + address + '\''
    s+= " WHERE lable =" + '\'' + supplier_name + '\''
    crsr.execute(s)
    connection.commit()

def update_transport():
    transporter_name = input("Enter name of transporter company which you want to update :")
    quantity = int(input("Enter new quantity: "))
    crsr = connection.cursor()
    s = "UPDATE transport SET "
    s += "quantity =" + str(quantity)
    s+= " WHERE company =" + '\'' + transporter_name + '\''
    crsr.execute(s)
    connection.commit()

def update_supplier_contact():
    old_phone_number = input("Enter phone_number of supplier_contact which you want to update :")
    phone_number = input("Enter new phone number: ")
    crsr = connection.cursor()
    s = "UPDATE supplier_contact SET "
    s += "phone_number =" + '\'' + phone_number + '\''

    s+= " WHERE phone_number =" + '\'' + old_phone_number + '\''
    crsr.execute(s)
    connection.commit()

def update_customer():
    customer_id = int(input("Enter customer id of customer which you want to update :"))
    name = input("Enter new name: ")
    house = input("Enter new house: ")
    street = input("Enter new street: ")
    city = input("Enter new city: ")
    state = input("Enter new state: ")
    crsr = connection.cursor()
    s = "UPDATE customer SET "
    s += "name =" + '\'' + name + '\'' + ','
    s += "house =" + '\'' + house + '\'' + ','
    s += "street =" + '\'' + street + '\'' + ','
    s += "city =" + '\'' + city + '\'' + ','
    s += "state =" + '\'' + state + '\'' + ' '
    s+= " WHERE customer_id =" + str(customer_id)
    crsr.execute(s)
    connection.commit()

def update_customer_contact():
    old_phone_number = input("Enter phone_number of customer_contact which you want to update :")
    phone_number = input("Enter new phone number: ")
    crsr = connection.cursor()
    s = "UPDATE customer_contact SET "
    s += "phone_number =" + '\'' + phone_number + '\''

    s+= " WHERE phone_number =" + '\'' + old_phone_number + '\''
    crsr.execute(s)
    connection.commit()

def update_employee():
    employee_id = int(input("Enter employee id of employee which you want to update :"))
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    address = input("Enter new address: ")
    crsr = connection.cursor()
    s = "UPDATE employee SET "
    s += "name =" + '\'' + name + '\'' + ','
    s += "address =" + '\'' + address + '\'' + ','
    s += "age =" + str(age)
    s+= " WHERE employee_id =" + str(employee_id)
    crsr.execute(s)
    connection.commit()

def update_job():
    designation = input("Enter designation of job which you want to update :")
    salary = int(input("Enter new salary: "))
    currently_working = int(input("Enter new currently_working: "))
    capacity = int(input("Enter new capacity: "))
    crsr = connection.cursor()
    s = "UPDATE job SET "
    s += "salary =" + str(salary) +','
    s += "currently_working =" + str(currently_working) +','
    s += "capacity =" + str(capacity) +','
    s += "vacancy =" + str(capacity-currently_working) 

    s+= " WHERE designation =" + '\'' + designation + '\''
    crsr.execute(s)
    connection.commit()

def update_ferry():
    product_id = int(input("Enter product id of the product whose ferry you want to update :"))
    outlet_id = int(input("Enter new outlet_id: "))
    supplier_name = input("Enter new supplier_name: ")
    transporter_name = input("Enter new transporter_name: ")
    crsr = connection.cursor()
    s = "UPDATE ferry SET "
    s += "supplier =" + '\'' + supplier_name + '\'' + ','
    s += "transport_company =" + '\'' + transporter_name + '\'' + ','
    s += "outlet_id =" + str(outlet_id)
    s+= " WHERE product_id =" + str(product_id)
    crsr.execute(s)
    connection.commit()

def update_billing():
    product_id = int(input("Enter product id of the product whose ferry you want to update :"))
    outlet_id = int(input("Enter new outlet_id: "))
    customer_id = int(input("Enter new customer_id: "))
    crsr = connection.cursor()
    s = "UPDATE billing SET "
    s += "outlet_id =" + str(outlet_id) +','
    s += "customer_id =" + str(customer_id)
    s+= " WHERE product_id =" + str(product_id)
    crsr.execute(s)
    connection.commit()

def update_worker():
    employee_id = int(input("Enter employee id of employee which you want to update :"))
    designation = input("Enter new designation: ")
    outlet_id = int(input("Enter new outlet_id: "))
    crsr = connection.cursor()
    s = "UPDATE worker SET "
    s += "designation =" + '\'' + designation + '\'' + ','
    s += "outlet_id =" + str(outlet_id)
    s+= " WHERE employee_id =" + str(employee_id)
    crsr.execute(s)
    connection.commit()

def delete_product():
    product_id = int(input("Enter product id of product which you want to delete :"))

    crsr = connection.cursor()
    s = "DELETE FROM product "
    s+= " WHERE product_id =" + str(product_id)
    crsr.execute(s)
    connection.commit()

def delete_outlet():
    outlet_id = int(input("Enter outlet id of outlet which you want to delete :"))

    crsr = connection.cursor()
    s = "DELETE FROM outlet "
    s+= " WHERE outlet_id =" + str(outlet_id)
    crsr.execute(s)
    connection.commit()

def delete_outlet_contact():
    old_phone_number = input("Enter phone_number of outlet_contact which you want to delete :")

    crsr = connection.cursor()
    s = "DELETE FROM outlet_contact "
    s+= " WHERE phone_number =" + '\'' + old_phone_number + '\''
    crsr.execute(s)
    connection.commit()

def delete_supplier():
    supplier_name = input("Enter name of supplier which you want to delete :")

    crsr = connection.cursor()
    s = "DELETE FROM supplier "
    s+= " WHERE lable =" + '\'' + supplier_name + '\''
    crsr.execute(s)
    connection.commit()

def delete_transport():
    transporter_name = input("Enter name of transporter company which you want to delete :")

    crsr = connection.cursor()
    s = "DELETE FROM transport "
    s+= " WHERE company =" + '\'' + transporter_name + '\''
    crsr.execute(s)
    connection.commit()

def delete_supplier_contact():
    old_phone_number = input("Enter phone_number of supplier_contact which you want to delete :")

    crsr = connection.cursor()
    s = "DELETE FROM supplier_contact "
    s+= " WHERE phone_number =" + '\'' + old_phone_number + '\''
    crsr.execute(s)
    connection.commit()

def delete_customer():
    customer_id = int(input("Enter customer id of customer which you want to delete :"))

    crsr = connection.cursor()
    s = "DELETE FROM customer "
    s+= " WHERE customer_id =" + str(customer_id)
    crsr.execute(s)
    connection.commit()

def delete_customer_contact():
    old_phone_number = input("Enter phone_number of customer_contact which you want to delete :")

    crsr = connection.cursor()
    s = "DELETE FROM customer_contact "
    s+= " WHERE phone_number =" + '\'' + old_phone_number + '\''
    crsr.execute(s)
    connection.commit()

def delete_employee():
    employee_id = int(input("Enter employee id of employee which you want to delete :"))

    crsr = connection.cursor()
    s = "DELETE FROM employee "
    s+= " WHERE employee_id =" + str(employee_id)
    crsr.execute(s)
    connection.commit()

def delete_job():
    designation = input("Enter designation of job which you want to delete :")

    crsr = connection.cursor()
    s = "DELETE FROM job "
    s+= " WHERE designation =" + '\'' + designation + '\''
    crsr.execute(s)
    connection.commit()

def delete_ferry():
    product_id = int(input("Enter product id of the product whose ferry you want to delete :"))

    crsr = connection.cursor()
    s = "DELETE FROM ferry "
    s+= " WHERE product_id =" + str(product_id)
    crsr.execute(s)
    connection.commit()

def delete_billing():
    product_id = int(input("Enter product id of the product whose ferry you want to delete :"))

    crsr = connection.cursor()
    s = "DELETE FROM billing "
    s+= " WHERE product_id =" + str(product_id)
    crsr.execute(s)
    connection.commit()

def delete_worker():
    employee_id = int(input("Enter employee id of employee which you want to delete :"))

    crsr = connection.cursor()
    s = "DELETE FROM worker "
    s+= " WHERE employee_id =" + str(employee_id) 
    crsr.execute(s)
    connection.commit()

def customer_from_city():
    city = input("Enter name of city: ")
    crsr = connection.cursor()
    print("details of customer from desired city ")
    s = "SELECT * FROM customer WHERE city =" + ( '\'' + city + '\'' ) 
    crsr.execute(s)
    crsr.execute(s)
    result = crsr.fetchall()
    for row in result:
        print(row)
    connection.commit()

def employee_younger_than():
    age = int(input("Enter threshold age: "))
    crsr = connection.cursor()
    print("employee younger than threshold age: ")
    s = "SELECT * FROM employee WHERE age < " + str(age)
    crsr.execute(s)
    result = crsr.fetchall()
    for row in result:
        print(row)
    connection.commit()

def select_outlet_with_product():
    product_id = int(input("Enter product_id: "))
    crsr = connection.cursor()
    print("outlet_id of outlets having desired product :")
    s = "SELECT outlet_id FROM ferry WHERE product_id = " + str(product_id) 
    crsr.execute(s)
    crsr.execute(s)
    result = crsr.fetchall()
    for row in result:
        print(row)
    connection.commit()

def products_needed():
    threshold_stock = int(input("Enter the amount of stock below which the product is needed: "))
    crsr = connection.cursor()
    print("Product_id of products needed are: \n")
    s = "SELECT product_id FROM product WHERE stock < " + str(threshold_stock) 
    
    crsr.execute(s)
    result = crsr.fetchall()
    for row in result:
        print(row)
    connection.commit()

def products_sold():
    crsr = connection.cursor()
    s = "SELECT COUNT() FROM billing ;"
    crsr.execute(s)
    result = crsr.fetchall()
    print("Number of products sold are: ")
    for row in result:
        print(row)
    connection.commit()

def search_employee():
    name = input("Enter the name of employee: ")
    crsr = connection.cursor()
    s = "SELECT * FROM employee WHERE name LIKE " + ( '\'' + name  + '\'' ) 
    
    crsr.execute(s)
    result = crsr.fetchall()
    for row in result:
        print(row)
    connection.commit()

def search_product():
    ID = input("Enter the product_id: ")
    crsr = connection.cursor()
    s = "SELECT * FROM product WHERE product_id LIKE " + ( '\'' + ID  + '\'' ) 
    
    crsr.execute(s)
    result = crsr.fetchall()
    for row in result:
        print(row)
    connection.commit()

def total_sale_in_day_on_outlet():
    outlet_id = int(input("Enter outlet_id: "))
    s = "SELECT product_id FROM ferry WHERE outlet_id = " + str(outlet_id) 
    crsr = connection.cursor()
    crsr.execute(s)
    result = crsr.fetchall()
    for row in result:
        for word in row:
            p = "SELECT * FROM product WHERE product_id ="+ str(word)
            crsr.execute(p)
            res = crsr.fetchall()
            for rw in res:
                print(rw)
    connection.commit()

def number_of_customers_in_outlet():
    outlet_id = int(input("Enter outlet_id: "))
    s = "SELECT customer_id FROM billing WHERE outlet_id = " + str(outlet_id) 
    crsr = connection.cursor()
    crsr.execute(s)
    result = crsr.fetchall()
    for row in result:
        for word in row:
            p = "SELECT * FROM customer WHERE customer_id ="+ str(word)
            crsr.execute(p)
            res = crsr.fetchall()
            for rw in res:
                print(rw)
    connection.commit()
    


def initialize():
    crsr = connection.cursor()
    crsr.execute("CREATE TABLE  IF NOT EXISTS product (product_id INTEGER PRIMARY KEY, retail_price INTEGER, wholesale_price INTEGER, stock INTEGER,profit INTEGET ) ")
    crsr.execute("CREATE TABLE  IF NOT EXISTS outlet (outlet_id INTEGER PRIMARY KEY, PIN INTERGER, state VARCHAR[20], city  VARCHAR[20], address  VARCHAR[20])")
    crsr.execute("CREATE TABLE  IF NOT EXISTS outlet_contact (outlet_id INTEGER REFERENCES outlet(outlet_id), phone_number varchar[20])")
    crsr.execute("CREATE TABLE  IF NOT EXISTS supplier (lable varchar[20],address varchar[20])")
    crsr.execute("CREATE TABLE  IF NOT EXISTS supplier_contact (lable varchar[20] REFERENCES supplier(lable),phone_number varchar[20])")
    crsr.execute("CREATE TABLE IF NOT EXISTS transport (company varchar[20],quantity INTEGER)")
    crsr.execute("CREATE TABLE IF NOT EXISTS customer (customer_id INTEGER PRIMARY KEY, name varchar[30],house varchar[30], street varchar[30], city varchar[30], state varchar[30])")
    crsr.execute("CREATE TABLE  IF NOT EXISTS customer_contact (customer_id INTEGER REFERENCES customer(customer_id), phone_number varchar[20])")
    crsr.execute("CREATE TABLE IF NOT EXISTS employee (employee_id INTEGER PRIMARY KEY, name varchar[30],age INT, address varchar[80])")
    crsr.execute("CREATE TABLE IF NOT EXISTS job (salary INTEGER, designation varchar[20], capacity INTEGER, currently_working INTEGER, vacancy INTEGER)")
    crsr.execute("CREATE TABLE  IF NOT EXISTS ferry (product_id INTEGER REFERENCES product(product_id), outlet_id INTEGER REFERENCES outlet(outlet_id),supplier varchar[20] REFERENCES supplier(lable),transport_company varchar[20] REFERENCES transport(company))")
    crsr.execute("CREATE TABLE  IF NOT EXISTS billing (product_id INTEGER REFERENCES product(product_id), outlet_id INTEGER REFERENCES outlet(outlet_id),customer_id INTEGER REFERENCES customer(customer_id))")
    crsr.execute("CREATE TABLE  IF NOT EXISTS worker (employee_id INTEGER REFERENCES employee(employee_id), outlet_id INTEGER REFERENCES outlet(outlet_id),designation varchar[20] REFERENCES job(designation))")

    


initialize()
while(1):
    string_1 = input("Enter command: ")

    if(string_1=="exit"):
        break

    if(string_1=="insert product"):
        insert_into_product()

    if(string_1=="insert outlet"):
        insert_into_outlet()

    if(string_1=="insert outlet_contact"):
        insert_into_outlet_contact()

    if(string_1=="insert supplier"):
        insert_into_supplier()

    if(string_1=="insert supplier_contact"):
        insert_into_supplier_contact()

    if(string_1=="insert transport"):
        insert_into_transport()

    if(string_1=="insert customer"):
        insert_into_customer()

    if(string_1=="insert customer_contact"):
        insert_into_customer_contact()

    if(string_1=="insert employee"):
        insert_into_employee()

    if(string_1=="insert job"):
        insert_into_job()

    if(string_1=="insert ferry"):
        insert_into_ferry()

    if(string_1=="insert billing"):
        insert_into_billing()
    
    if(string_1=="insert worker"):
        insert_into_worker()

    if(string_1=="update product"):
        update_product()

    if(string_1=="update outlet"):
        update_outlet()

    if(string_1=="update outlet_contact"):
        update_outlet_contact()
        
    if(string_1=="update supplier"):
        update_supplier()

    if(string_1=="update supplier_contact"):
        update_supplier_contact()

    if(string_1=="update transport"):
        update_transport()   

    if(string_1=="update customer"):
        update_customer()

    if(string_1=="update customer_contact"):
        update_customer_contact()

    if(string_1=="update employee"):
        update_employee()

    if(string_1=="update job"):
        update_job()

    if(string_1=="update ferry"):
        update_ferry()

    if(string_1=="update billing"):
        update_billing()
    
    if(string_1=="update worker"):
        update_worker()

    if(string_1=="delete product"):
        delete_product()

    if(string_1=="delete outlet"):
        delete_outlet()

    if(string_1=="delete outlet_contact"):
        delete_outlet_contact()
        
    if(string_1=="delete supplier"):
        delete_supplier()

    if(string_1=="delete supplier_contact"):
        delete_supplier_contact()

    if(string_1=="delete transport"):
        delete_transport()   

    if(string_1=="delete customer"):
        delete_customer()

    if(string_1=="delete customer_contact"):
        delete_customer_contact()

    if(string_1=="delete employee"):
        delete_employee()

    if(string_1=="delete job"):
        delete_job()

    if(string_1=="delete ferry"):
        delete_ferry()

    if(string_1=="delete billing"):
        delete_billing()
    
    if(string_1=="delete worker"):
        delete_worker()

    if(string_1=="customer from city"):
        customer_from_city()

    if(string_1 == "employee younger than"):
        employee_younger_than()

    if(string_1 == "select outlet with product"):
        select_outlet_with_product()
    
    if(string_1 == "products needed"):
        products_needed()

    if(string_1 == "products sold"):
        products_sold()

    if(string_1 == "search employee"):
        search_employee()

    if(string_1 == "search product"):
        search_product()

    if(string_1 == "total sale in day on outlet"):
        total_sale_in_day_on_outlet()

    if(string_1 == "number of customers in outlet"):
        number_of_customers_in_outlet()

