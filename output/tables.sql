
        DROP TABLE IF EXISTS OMJunc, MIJunc, Orders, Menu, Inventory, Employees CASCADE;
        DROP TYPE IF EXISTS menu_category;

        CREATE TABLE Employees (
            id INT PRIMARY KEY,
            employeeName TEXT NOT NULL,
            position TEXT NOT NULL,
            email TEXT NOT NULL
        );
        


        CREATE TABLE Orders (
            id INT PRIMARY KEY,
            customerName TEXT NOT NULL,
            time TIMESTAMP NOT NULL,
            paid DECIMAL(10,2) NOT NULL,
            EmployeeID INT NOT NULL,
            FOREIGN KEY (EmployeeID) REFERENCES Employees(id)
        );
        


        CREATE TYPE MENU_CATEGORY AS ENUM ('Limited Time Offers', 'Value Meals', 'Burgers', 'Sandwiches', 'Salads', 'Deserts', 'Appetizers', 'Beverages');
        
        CREATE TABLE Menu (
            id INT PRIMARY KEY,
            itemName TEXT NOT NULL,
            price DECIMAL(10,2) NOT NULL,
            category MENU_CATEGORY NOT NULL
        );
        


        CREATE TABLE OMJunc (
            id INT PRIMARY KEY,
            menuID INT NOT NULL,
            orderID INT NOT NULL,
            FOREIGN KEY (menuID) REFERENCES Menu(id),
            FOREIGN KEY (orderID) REFERENCES Orders(id)
        );
        


        CREATE TABLE Inventory (
            id INT PRIMARY KEY,
            name TEXT NOT NULL,
            stock INT NOT NULL,
            location TEXT NOT NULL,
            capacity INT NOT NULL,
            supplier TEXT NOT NULL,
            minimum INT NOT NULL
        );
        


        CREATE TABLE MIJunc (
            id INT PRIMARY KEY,
            menuID INT NOT NULL,
            itemID INT NOT NULL,
            itemAmount DECIMAL(10,2) NOT NULL,
            FOREIGN KEY (menuID) REFERENCES Menu(id),
            FOREIGN KEY (itemID) REFERENCES Inventory(id)
        );
        


        INSERT INTO Menu (id, itemName, price, category)
        VALUES (1, 'Tender Entree', 4.99, 'Value Meals');
        


        INSERT INTO Menu (id, itemName, price, category)
        VALUES (2, 'Corn Dog Value Meal', 4.99, 'Value Meals');
        


        INSERT INTO Menu (id, itemName, price, category)
        VALUES (3, '2 Hot Dog Value Meal', 4.99, 'Value Meals');
        


        INSERT INTO Menu (id, itemName, price, category)
        VALUES (4, 'Bacon Cheeseburger', 8.29, 'Burgers');
        


        INSERT INTO Menu (id, itemName, price, category)
        VALUES (5, 'Black Bean Burger', 7.59, 'Burgers');
        


        INSERT INTO Menu (id, itemName, price, category)
        VALUES (6, 'Cheeseburger', 6.89, 'Burgers');
        


        INSERT INTO Menu (id, itemName, price, category)
        VALUES (7, 'Gig Em Patty Melt', 7.59, 'Burgers');
        


        INSERT INTO Menu (id, itemName, price, category)
        VALUES (8, 'Classic Hamburger', 6.89, 'Burgers');
        


        INSERT INTO Menu (id, itemName, price, category)
        VALUES (9, 'Aggie Chicken Club', 8.39, 'Sandwiches');
        


        INSERT INTO Menu (id, itemName, price, category)
        VALUES (10, 'Revs Grilled Chicken Sandwich', 8.39, 'Sandwiches');
        


        INSERT INTO Menu (id, itemName, price, category)
        VALUES (11, 'Spicy Chicken Sandwich', 8.39, 'Sandwiches');
        


        INSERT INTO Menu (id, itemName, price, category)
        VALUES (12, 'Chicken Caesar Salad', 8.29, 'Salads');
        


        INSERT INTO Menu (id, itemName, price, category)
        VALUES (13, 'Double Scoop Ice Cream', 3.29, 'Deserts');
        


        INSERT INTO Menu (id, itemName, price, category)
        VALUES (14, 'Aggie Shakes', 4.49, 'Deserts');
        


        INSERT INTO Menu (id, itemName, price, category)
        VALUES (15, 'Cookie Ice Cream Sundae', 4.69, 'Deserts');
        


        INSERT INTO Menu (id, itemName, price, category)
        VALUES (16, 'Root Bear Float', 5.49, 'Deserts');
        


        INSERT INTO Menu (id, itemName, price, category)
        VALUES (17, 'French Fries', 1.99, 'Appetizers');
        


        INSERT INTO Menu (id, itemName, price, category)
        VALUES (18, 'Aquafina Water 16OZ', 1.79, 'Beverages');
        


        INSERT INTO Menu (id, itemName, price, category)
        VALUES (19, 'Aquafina Water 20OZ', 2.39, 'Beverages');
        


        INSERT INTO Menu (id, itemName, price, category)
        VALUES (20, 'Pepsi Fountain 20OZ', 1.99, 'Beverages');
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (1, 'Napkins', 100, 'Cabinet 10', 1000, 'Nap Inc.', 50);
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (2, 'Chicken', 50, 'Cabinet 1', 75, 'Local Farm', 15);
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (3, 'Beef Patty', 20, 'Cabinet 3', 2000, 'Local Farm', 25);
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (4, 'Oil', 5000, 'Cabinet 8', 5500, 'Saudi Inc.', 500);
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (5, 'Salt', 3000, 'Cabinet 12', 10000, 'Saltine Inc.', 1000);
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (6, 'Buns', 200, 'Cabinet 13', 400, 'BreadBake Inc.', 100);
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (7, 'Lettuce', 25, 'Cabinet 21', 100, 'Local Farm', 50);
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (8, 'Tomato', 40, 'Cabinet 10', 100, 'Local Farm', 50);
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (9, 'Onion', 35, 'Cabinet 10', 100, 'Local Farm', 50);
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (10, 'Potato', 100, 'Cabinet 15', 1500, 'Idaho Inc.', 75);
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (11, 'Ketchup', 1500, 'Cabinet 17', 2000, 'Heinz', 250);
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (12, 'Paper Towels', 500, 'Cabinet 9', 1000, 'Nap Inc.', 50);
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (13, 'Pepper', 5500, 'Cabinet 10', 10000, 'Doctor Pep Inc.', 150);
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (14, 'Drink Cup', 25, 'Cabinet 23', 300, 'Juice Inc.', 50);
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (15, 'Pickles', 80, 'Cabinet 21', 150, 'PickPick Inc.', 20);
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (16, 'Ice Cream', 10, 'Cabinet 16', 200, 'Creamers Inc.', 25);
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (17, 'Hot Dog', 100, 'Cabinet 19', 1000, 'Dawg Inc.', 75);
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (18, 'Cheese', 75, 'Cabinet 30', 5000, 'Seech Inc.', 200);
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (19, 'Bacon', 120, 'Cabinet 31', 250, 'Nacob Inc.', 35);
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (20, 'Black Bean', 32, 'Cabinet 34', 500, 'Bean Inc.', 40);
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (21, 'Toast', 50, 'Cabinet 21', 150, 'Yeast Inc.', 25);
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (22, 'Gravy', 12, 'Cabinet 13', 100, 'Gravity Inc.', 20);
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (23, 'Hot Dog Bun', 100, 'Cabinet 1', 120, 'Doggy Inc.', 25);
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (24, 'Gig Em Sauce', 120, 'Cabinet 12', 400, 'TAMU Inc.', 40);
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (25, 'Spice', 25, 'Cabinet 11', 50, 'Pepper Inc.', 10);
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (26, 'Milk', 10, 'Fridge 2', 20, 'Moo Moo Inc.', 10);
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (27, 'Cookies', 10, 'Fridge 1', 50, 'Moo Moo Inc.', 5);
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (28, 'Water Bottles', 200, 'Fridge 2', 1000, 'Ozark Inc.', 100);
        


        INSERT INTO Inventory (id, name, stock, location, capacity, supplier, minimum)
        VALUES (29, 'Soda', 500, 'Cooler', 4000, 'Doctor Salt Inc.', 250);
        


        INSERT INTO Employees (id, employeeName, position, email)
        VALUES (1, 'Oz', 'Admin', 'ozjohnson@gmail.com');
        


        INSERT INTO Employees (id, employeeName, position, email)
        VALUES (2, 'Nolan', 'Cashier', 'nolanryan@gmail.com');
        


        INSERT INTO Employees (id, employeeName, position, email)
        VALUES (3, 'Jimothy', 'Manager', 'jimothyrockwell@gmail.com');
        


        INSERT INTO Employees (id, employeeName, position, email)
        VALUES (4, 'Rebecca', 'Cashier', 'rebeccastone@gmail.com');
        


        INSERT INTO Employees (id, employeeName, position, email)
        VALUES (5, 'George', 'Cashier', 'georgetyson@gmail.com');
        


        INSERT INTO Employees (id, employeeName, position, email)
        VALUES (6, 'Kylie', 'Cashier', 'kyliek1234@gmail.com');
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (1, 1, 2, 3);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (2, 1, 10, 2);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (3, 1, 5, 6);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (4, 1, 11, 2);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (5, 1, 4, 4);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (6, 1, 21, 1);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (7, 1, 22, 1);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (8, 2, 11, 1);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (9, 2, 17, 1);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (10, 2, 5, 6);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (11, 3, 11, 1);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (12, 3, 17, 1);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (13, 3, 23, 1);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (14, 3, 5, 6);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (15, 4, 19, 2);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (16, 4, 18, 1);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (17, 4, 6, 2);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (18, 4, 3, 1);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (19, 4, 5, 6);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (20, 5, 20, 6);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (21, 5, 6, 2);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (22, 6, 18, 1);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (23, 6, 6, 2);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (24, 6, 3, 1);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (25, 6, 5, 6);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (26, 6, 15, 3);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (27, 7, 18, 1);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (28, 7, 21, 2);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (29, 7, 3, 1);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (30, 7, 5, 6);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (31, 7, 9, 6);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (32, 7, 24, 1);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (33, 8, 6, 2);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (34, 8, 3, 1);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (35, 8, 5, 6);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (36, 8, 8, 1);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (37, 8, 7, 1);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (38, 8, 9, 6);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (39, 8, 15, 3);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (40, 9, 5, 6);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (41, 9, 2, 6);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (42, 9, 7, 1);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (43, 9, 9, 6);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (44, 9, 8, 1);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (45, 9, 15, 3);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (46, 9, 6, 2);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (47, 10, 5, 6);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (48, 10, 2, 3);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (49, 10, 21, 2);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (50, 10, 18, 1);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (51, 10, 24, 1);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (52, 1, 5, 6);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (53, 1, 2, 3);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (54, 1, 21, 2);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (55, 1, 18, 1);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (56, 11, 24, 1);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (57, 11, 25, 1);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (58, 12, 7, 6);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (59, 12, 18, 1);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (60, 12, 24, 1);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (61, 12, 21, 1);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (62, 13, 16, 2);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (63, 14, 16, 2);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (64, 14, 26, 2);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (65, 15, 16, 2);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (66, 15, 27, 2);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (67, 16, 16, 2);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (68, 16, 29, 2);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (69, 17, 10, 4);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (70, 17, 4, 6);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (71, 17, 5, 6);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (72, 17, 11, 2);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (73, 18, 28, 1);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (74, 19, 28, 2);
        


        INSERT INTO MIJunc (id, menuID, itemID, itemAmount)
        VALUES (75, 20, 29, 200);
        

