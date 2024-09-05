from data_script import menu, inventory, employees, MIJunc
from database_script import (
    create_table_commands,
    insert_menu_commands,
    insert_inventory_commands,
    insert_employees_commands,
    insert_mijunc_commands,
    write_commands_to_file
)
from orders_script import generate_order_csv

def main():
    # Generate SQL commands for table creation
    sql_commands = create_table_commands()

    # Generate SQL commands for inserting data
    sql_commands.extend(insert_menu_commands(menu))
    sql_commands.extend(insert_inventory_commands(inventory))
    sql_commands.extend(insert_employees_commands(employees))
    sql_commands.extend(insert_mijunc_commands(MIJunc))

    # Write SQL commands to a sql file
    write_commands_to_file(sql_commands, "../output/tables.sql")

    # Generate orders and write them to CSV files
    order_csv_path = '../output/orders.csv'
    omjunc_csv_path = '../output/omjunc.csv'
    num_days = 365  
    generate_order_csv(order_csv_path, omjunc_csv_path, num_days)

    print("SQL file created successfully!")

if __name__ == "__main__":
    main()