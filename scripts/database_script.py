def create_table_commands():
    table_commands = [
        """
        DROP TABLE IF EXISTS OMJunc, MIJunc, Orders, Menu, Inventory, Employees CASCADE;
        DROP TYPE IF EXISTS menu_category;
        """,

        """
        CREATE TABLE Employees (
            id INT PRIMARY KEY,
            employeeName TEXT NOT NULL,
            position TEXT NOT NULL,
            email TEXT NOT NULL
        );
        """,
      
        """
        CREATE TABLE Orders (
            id INT PRIMARY KEY,
            customerName TEXT NOT NULL,
            time TIMESTAMP NOT NULL,
            paid DECIMAL(10,2) NOT NULL,
            EmployeeID INT NOT NULL,
            FOREIGN KEY (EmployeeID) REFERENCES Employees(id)
        );
        """,

        """
        CREATE TYPE MENU_CATEGORY AS ENUM ('Limited Time Offers', 'Value Meals', 'Burgers', 'Sandwiches', 'Salads', 'Deserts', 'Appetizers', 'Beverages');
        
        CREATE TABLE Menu (
            id INT PRIMARY KEY,
            itemName TEXT NOT NULL,
            price DECIMAL(10,2) NOT NULL,
            category MENU_CATEGORY NOT NULL
        );
        """,

        """
        CREATE TABLE OMJunc (
            id INT PRIMARY KEY,
            menuID INT NOT NULL,
            orderID INT NOT NULL,
            FOREIGN KEY (menuID) REFERENCES Menu(id),
            FOREIGN KEY (orderID) REFERENCES Orders(id)
        );
        """,

        """
        CREATE TABLE Inventory (
            id INT PRIMARY KEY,
            name TEXT NOT NULL,
            stock INT NOT NULL,
            location TEXT NOT NULL,
            capacity INT NOT NULL,
            supplier TEXT NOT NULL,
            minimum INT NOT NULL
        );
        """,

        """
        CREATE TABLE MIJunc (
            id INT PRIMARY KEY,
            menuID INT NOT NULL,
            itemID INT NOT NULL,
            itemAmount DECIMAL(10,2) NOT NULL,
            FOREIGN KEY (menuID) REFERENCES Menu(id),
            FOREIGN KEY (itemID) REFERENCES Inventory(id)
        );
        """
    ]
    return table_commands


def insert_menu_commands(menu):
    commands = []
    for index, (key, price) in enumerate(menu.items(), start=1):
        item = key[3:]
        command = f"""
        INSERT INTO Menu (id, itemName, price)
        VALUES ({index}, '{item}', {price});
        """
        commands.append(command)
    return commands


def insert_inventory_commands(inventory):
    commands = []
    for index, (key, details) in enumerate(inventory.items(), start=1):
        stock = details['stock']
        location = details['location']
        capacity = details['capacity']
        supplier = details['supplier']
        name = details['name']
        minimum = details['minimum']
        command = f"""
        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES ({index}, '{name}', {stock}, '{location}', {capacity}, '{supplier}', {minimum});
        """
        commands.append(command)
    return commands


def insert_employees_commands(employees):
    commands = []
    for index, (key, details) in enumerate(employees.items(), start=1):
        name = details['name']
        position = details['position']
        email = details['email']
        command = f"""
        INSERT INTO Employees (id, employeeName, position, email)
        VALUES ({index}, '{name}', '{position}', '{email}');
        """
        commands.append(command)
    return commands


def insert_mijunc_commands(MIJunc):
    commands = []
    for index, (key, details) in enumerate(MIJunc.items(), start=1):
        menuID = details['menuID']
        itemID = details['itemID']
        itemAmount = details['itemAmount']
        command = f"""
        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES ({index}, {menuID}, {itemID}, {itemAmount});
        """
        commands.append(command)
    return commands


def write_commands_to_file(commands, filepath):
    with open(filepath, "w") as f:
        for command in commands:
            f.write(command + "\n\n")
