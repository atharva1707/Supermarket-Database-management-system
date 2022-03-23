## DATABASE FOR A CHAIN OF SUPERMARKET OUTLETS

### TABLES
> - product
> - outlet
> - outlet_contact
> - supplier
> - supplier_contact
> - transport
> - customer
> - customer_contact
> - employee
> - job
> - ferry
> - billing
> - worker



### Basic functions (insert, update, delete)
insert a new row in a table,
update an existing row in a table,
delete an existing row in a table.

Syntax
> - insert <table_name>
> - update <table_name>
> - delete <table_name>

### Additional functions

1.) customer_from_city()

    syntax: customer from city
> - The function will first ask for the desired city
> - The function displays all the rows in the customer table for which the city attribute matches with the desired city.

2.) employee_younger_than()

    syntax: employee younger than
> - The function will first ask for the threshold age
> - The function displays all the rows in the employee table for which the age is less than the threshold age.

3.) select_outlet_with_product()

    syntax: outlet with product
> - The function will first ask for the product_id
> - The function displays all the outlets that has the product corresponding to the desired product_id
> - It uses the billing table for this task

4.) products_needed()

    syntax: products needed
> - The function will first ask for a threshold stock
> - It then displays product id of all the products having stock less than threshold stock

5.) products_sold

    syntax: products sold
> - gives the count of all the product stored
> - uses the billing table for it

6.) search_employee()

    syntax: search employee
> - Searches for an employee using its name in the employee table

7.) search_product()

    syntax: search product
> - Searches for a product using its id in the product table

8.) total_sale_in_day_on_outlet()      

    syntax: total sale in day on outlet
> - Searches for the product_id of all the product sold from an outlet using the billing table
> - then it displays the corresponding row to the product_id in the product table

9.) number_of_customers_in_outlet()      

    syntax: number of customers outlet
> - Searches for the customer_id of all the customers that visited a particular outlet.
> - then it displays the corresponding row to the customer_id in the customer table