# Data for menu
menu = {
    "01 Tender Entree": 4.99, #Tender Entree
    "02 Corn Dog Value Meal": 4.99, #2 Corn Dog Value Meal
    "03 2 Hot Dog Value Meal": 4.99, #2 Hot Dog Value Meal
    "04 Bacon Cheeseburger": 8.29, #Bacon Cheeseburgers
    "05 Black Bean Burger": 7.59, #Black Bean Burger
    "06 Cheeseburger": 6.89, #Cheeseburger
    "07 Gig Em Patty Melt": 7.59, #Gig Em Patty Melt
    "08 Classic Hamburger": 6.89, #Classic Hamburger
    "09 Aggie Chicken Club": 8.39, #Aggie Chicken Club
    "10 Revs Grilled Chicken Sandwich": 8.39, #Revs Grilled Chicken Sandwich
    "11 Spicy Chicken Sandwich": 8.39, #Spicy Chicken Sandwich
    "12 Chicken Caesar Salad": 8.29, #Chicken Caesar Salad
    "13 Double Scoop Ice Cream": 3.29, #Double Scoop Ice Cream
    "14 Aggie Shakes": 4.49, #Aggie Shakes
    "15 Cookie Ice Cream Sundae": 4.69, #Cookie Ice Cream Sundae
    "16 Root Bear Float": 5.49, #Root Bear Float
    "17 French Fries": 1.99, #French Fries
    "18 Aquafina Water 16OZ": 1.79, #Aquafina Water 16OZ
    "19 Aquafina Water 20OZ": 2.39, #Aquafina Water 20OZ
    "20 Pepsi Fountain 20OZ": 1.99, #Pepsi Fountain 20OZ
}


# Data for inventory
inventory = {
    "01 Napkins": {
        "stock": 100,
        "location": "Cabinet 10",
        "capacity": 1000,
        "supplier": "Nap Inc.",
        "name": "Napkins",
        "minimum": 50
    },
    "02 Chicken": {
        "stock": 50,
        "location": "Cabinet 1",
        "capacity": 75,
        "supplier": "Local Farm",
        "name": "Chicken",
        "minimum": 15
    },
    "03 Beef Patty": {
        "stock": 20,
        "location": "Cabinet 3",
        "capacity": 2000,
        "supplier": "Local Farm",
        "name": "Beef Patty",
        "minimum": 25
    },
    "04 Oil": {
        "stock": 5000,
        "location": "Cabinet 8",
        "capacity": 5500,
        "supplier": "Saudi Inc.",
        "name": "Oil",
        "minimum": 500
    },
    "05 Salt": {
        "stock": 3000,
        "location": "Cabinet 12",
        "capacity": 10000,
        "supplier": "Saltine Inc.",
        "name": "Salt",
        "minimum": 1000
    },
    "06 Buns": {
        "stock": 200,
        "location": "Cabinet 13",
        "capacity": 400,
        "supplier": "BreadBake Inc.",
        "name": "Buns",
        "minimum": 100
    },
    "07 Lettuce": {
        "stock": 25,
        "location": "Cabinet 21",
        "capacity": 100,
        "supplier": "Local Farm",
        "name": "Lettuce",
        "minimum": 50
    },
    "08 Tomato": {
        "stock": 40,
        "location": "Cabinet 10",
        "capacity": 100,
        "supplier": "Local Farm",
        "name": "Tomato",
        "minimum": 50
    },
    "09 Onion": {
        "stock": 35,
        "location": "Cabinet 10",
        "capacity": 100,
        "supplier": "Local Farm",
        "name": "Onion",
        "minimum": 50
    },
    "10 Potato": {
        "stock": 100,
        "location": "Cabinet 15",
        "capacity": 1500,
        "supplier": "Idaho Inc.",
        "name": "Potato",
        "minimum": 75
    },
    "11 Ketchup": {
        "stock": 1500,
        "location": "Cabinet 17",
        "capacity": 2000,
        "supplier": "Heinz",
        "name": "Ketchup",
        "minimum": 250
    },
    "12 Paper Towels": {
        "stock": 500,
        "location": "Cabinet 9",
        "capacity": 1000,
        "supplier": "Nap Inc.",
        "name": "Paper Towels",
        "minimum": 50
    },
    "13 Pepper": {
        "stock": 5500,
        "location": "Cabinet 10",
        "capacity": 10000,
        "supplier": "Doctor Pep Inc.",
        "name": "Pepper",
        "minimum": 150
    },
    "14 Drink Cup": {
        "stock": 25,
        "location": "Cabinet 23",
        "capacity": 300,
        "supplier": "Juice Inc.",
        "name": "Drink Cup",
        "minimum": 50
    },
    "15 Pickles": {
        "stock": 80,
        "location": "Cabinet 21",
        "capacity": 150,
        "supplier": "PickPick Inc.",
        "name": "Pickles",
        "minimum": 20
    },
    "16 Ice Cream": {
        "stock": 10,
        "location": "Cabinet 16",
        "capacity": 200,
        "supplier": "Creamers Inc.",
        "name": "Ice Cream",
        "minimum": 25
    },
    "17 Hot Dog": {
        "stock": 100,
        "location": "Cabinet 19",
        "capacity": 1000,
        "supplier": "Dawg Inc.",
        "name": "Hot Dog",
        "minimum": 75
    },
    "18 Cheese": {
        "stock": 75,
        "location": "Cabinet 30",
        "capacity": 5000,
        "supplier": "Seech Inc.",
        "name": "Cheese",
        "minimum": 200
    },
    "19 Bacon": {
        "stock": 120,
        "location": "Cabinet 31",
        "capacity": 250,
        "supplier": "Nacob Inc.",
        "name": "Bacon",
        "minimum": 35
    },
    "20 Black Bean": {
        "stock": 32,
        "location": "Cabinet 34",
        "capacity": 500,
        "supplier": "Bean Inc.",
        "name": "Black Bean",
        "minimum": 40
    },
    "21 Toast": {
        "stock": 50,
        "location": "Cabinet 21",
        "capacity": 150,
        "supplier": "Yeast Inc.",
        "name": "Toast",
        "minimum": 25
    },
    "22 Gravy": {
        "stock": 12,
        "location": "Cabinet 13",
        "capacity": 100,
        "supplier": "Gravity Inc.",
        "name": "Gravy",
        "minimum": 20
    },
    "23 Hot Dog Bun": {
        "stock": 100,
        "location": "Cabinet 1",
        "capacity": 120,
        "supplier": "Doggy Inc.",
        "name": "Hot Dog Bun",
        "minimum": 25
    },
    "24 Gig Em Sauce": {
        "stock": 120,
        "location": "Cabinet 12",
        "capacity": 400,
        "supplier": "TAMU Inc.",
        "name": "Gig Em Sauce",
        "minimum": 40
    },
    "25 Spice": {
        "stock": 25,
        "location": "Cabinet 11",
        "capacity": 50,
        "supplier": "Pepper Inc.",
        "name": "Spice",
        "minimum": 10
    },
    "26 Milk": {
        "stock": 10,
        "location": "Fridge 2",
        "capacity": 20,
        "supplier": "Moo Moo Inc.",
        "name": "Milk",
        "minimum": 10
    },
    "27 Cookies": {
        "stock": 10,
        "location": "Fridge 1",
        "capacity": 50,
        "supplier": "Moo Moo Inc.",
        "name": "Cookies",
        "minimum": 5
    },
    "28 Water Bottles": {
        "stock": 200,
        "location": "Fridge 2",
        "capacity": 1000,
        "supplier": "Ozark Inc.",
        "name": "Water Bottles",
        "minimum": 100
    },
    "29 Soda": {
        "stock": 500,
        "location": "Cooler",
        "capacity": 4000,
        "supplier": "Doctor Salt Inc.",
        "name": "Soda",
        "minimum": 250
    },
}


# Data for employees
employees = {
    "Oz": {
        "name": "Oz",
        "position": "Admin",
        "email": "ozjohnson@gmail.com"
    },
    "Nolan": {
        "name": "Nolan",
        "position": "Cashier",
        "email": "nolanryan@gmail.com"
    },
    "Jimothy": {
        "name": "Jimothy",
        "position": "Manager",
        "email": "jimothyrockwell@gmail.com"
    },
    "Rebecca": {
        "name": "Rebecca",
        "position": "Cashier",
        "email": "rebeccastone@gmail.com"
    },
    "George": {
        "name": "George",
        "position": "Cashier",
        "email": "georgetyson@gmail.com"
    },
    "Kylie": {
        "name": "Kylie",
        "position": "Cashier",
        "email": "kyliek1234@gmail.com"
    },
}


# Data for MIJunc (Menu-Inventory Junction)
MIJunc = {
    "Tender Entree & Chicken": {
        "menuID": 1, 
        "itemID": 2,
        "itemAmount": 3
    },
    "Tender Entree & Potato": {
        "menuID": 1, 
        "itemID": 10,
        "itemAmount": 2
    },
    "Tender Entree & Salt": {
        "menuID": 1, 
        "itemID": 5,
        "itemAmount": 6
    },
    "Tender Entree & Ketchup": {
        "menuID": 1, 
        "itemID": 11,
        "itemAmount": 2
    },
    "Tender Entree & Oil": {
        "menuID": 1, 
        "itemID": 4,
        "itemAmount": 4
    },
    "Tender Entree & Toast": {
        "menuID": 1, 
        "itemID": 21,
        "itemAmount": 1
    },
    "Tender Entree & Gravy": {
        "menuID": 1, 
        "itemID": 22,
        "itemAmount": 1
    },
    "Corn Dog & Ketchup": {
        "menuID": 2, 
        "itemID": 11,
        "itemAmount": 1
    },
    "Corn Dog & Hot Dog": {
        "menuID": 2, 
        "itemID": 17,
        "itemAmount": 1
    },
    "Corn Dog & Ketchup": {
        "menuID": 2, 
        "itemID": 11,
        "itemAmount": 1
    },
    "Corn Dog & Hot Dog": {
        "menuID": 2, 
        "itemID": 17,
        "itemAmount": 1
    },
    "Corn Dog & Salt": {
        "menuID": 2, 
        "itemID": 5,
        "itemAmount": 6
    },
    "Hot Dog & Ketchup": {
        "menuID": 3, 
        "itemID": 11,
        "itemAmount": 1
    },
    "Hot Dog & Hot Dog": {
        "menuID": 3, 
        "itemID": 17,
        "itemAmount": 1
    },
    "Hot Dog & Hot Dog Bun": {
        "menuID": 3, 
        "itemID": 23,
        "itemAmount": 1
    },
    "Hot Dog & Salt": {
        "menuID": 3, 
        "itemID": 5,
        "itemAmount": 6
    },
    "Bacon Cheeseburger & Bacon": {
        "menuID": 4, 
        "itemID": 19,
        "itemAmount": 2
    },
    "Bacon Cheeseburger & Cheese": {
        "menuID": 4, 
        "itemID": 18,
        "itemAmount": 1
    },
    "Bacon Cheeseburger & Buns": {
        "menuID": 4, 
        "itemID": 6,
        "itemAmount": 2
    },
    "Bacon Cheeseburger & Beef Patty": {
        "menuID": 4, 
        "itemID": 3,
        "itemAmount": 1
    },
    "Bacon Cheeseburger & Salt": {
        "menuID": 4, 
        "itemID": 5,
        "itemAmount": 6
    },
    "Black Bean Burger & Black Bean": {
        "menuID": 5, 
        "itemID": 20,
        "itemAmount": 6
    },
    "Black Bean Burger & Buns": {
        "menuID": 5, 
        "itemID": 6,
        "itemAmount": 2
    },
    "Cheeseburger & Cheese": {
        "menuID": 6, 
        "itemID": 18,
        "itemAmount": 1
    },
    "Cheeseburger & Buns": {
        "menuID": 6, 
        "itemID": 6,
        "itemAmount": 2
    },
    "Cheeseburger & Beef Patty": {
        "menuID": 6, 
        "itemID": 3,
        "itemAmount": 1
    },
    "Cheeseburger & Salt": {
        "menuID": 6, 
        "itemID": 5,
        "itemAmount": 6
    },
    "Cheeseburger & Pickles": {
        "menuID": 6, 
        "itemID": 15,
        "itemAmount": 3
    },
    "Patty Melt & Cheese": {
        "menuID": 7, 
        "itemID": 18,
        "itemAmount": 1
    },
    "Patty Melt & Toast": {
        "menuID": 7, 
        "itemID": 21,
        "itemAmount": 2
    },
    "Patty Melt & Beef Patty": {
        "menuID": 7, 
        "itemID": 3,
        "itemAmount": 1
    },
    "Patty Melt & Salt": {
        "menuID": 7, 
        "itemID": 5,
        "itemAmount": 6
    },
    "Patty Melt & Onions": {
        "menuID": 7, 
        "itemID": 9,
        "itemAmount": 6
    },
    "Patty Melt & Sauce": {
        "menuID": 7, 
        "itemID": 24,
        "itemAmount": 1
    },
    "Hamburger & Buns": {
        "menuID": 8, 
        "itemID": 6,
        "itemAmount": 2
    },
    "Hamburger & Beef Patty": {
        "menuID": 8, 
        "itemID": 3,
        "itemAmount": 1
    },
    "Hamburger & Salt": {
        "menuID": 8, 
        "itemID": 5,
        "itemAmount": 6
    },
    "Hamburger & Tomato": {
        "menuID": 8, 
        "itemID": 8,
        "itemAmount": 1
    },
    "Hamburger & Lettuce": {
        "menuID": 8, 
        "itemID": 7,
        "itemAmount": 1
    },
    "Hamburger & Onions": {
        "menuID": 8, 
        "itemID": 9,
        "itemAmount": 6
    },
    "Hamburger & Pickles": {
        "menuID": 8, 
        "itemID": 15,
        "itemAmount": 3
    },
    "Chicken Club & Salt": {
        "menuID": 9, 
        "itemID": 5,
        "itemAmount": 6
    },
    "Chicken Club & Chicken": {
        "menuID": 9, 
        "itemID": 2,
        "itemAmount": 6
    },
    "Chicken Club & Lettuce": {
        "menuID": 9, 
        "itemID": 7,
        "itemAmount": 1
    },
    "Chicken Club & Onions": {
        "menuID": 9, 
        "itemID": 9,
        "itemAmount": 6
    },
    "Chicken Club & Tomato": {
        "menuID": 9, 
        "itemID": 8,
        "itemAmount": 1
    },
    "Chicken Club & Pickles": {
        "menuID": 9, 
        "itemID": 15,
        "itemAmount": 3
    },
    "Chicken Club & Buns": {
        "menuID": 9, 
        "itemID": 6,
        "itemAmount": 2
    },
    "Chicken Sandwich & Salt": {
        "menuID": 10, 
        "itemID": 5,
        "itemAmount": 6
    },
    "Chicken Sandwich & Chicken": {
        "menuID": 10, 
        "itemID": 2,
        "itemAmount": 3
    },
    "Chicken Sandwich & Toast": {
        "menuID": 10, 
        "itemID": 21,
        "itemAmount": 2
    },
    "Chicken Sandwich & Cheese": {
        "menuID": 10, 
        "itemID": 18,
        "itemAmount": 1
    },
    "Chicken Sandwich & Sauce": {
        "menuID": 10, 
        "itemID": 24,
        "itemAmount": 1
    },
    "Spicy Chicken Sandwich & Salt": {
        "menuID": 1, 
        "itemID": 5,
        "itemAmount": 6
    },
    "Spicy Chicken Sandwich & Chicken": {
        "menuID": 1, 
        "itemID": 2,
        "itemAmount": 3
    },
    "Spicy Chicken Sandwich & Toast": {
        "menuID": 1, 
        "itemID": 21,
        "itemAmount": 2
    },
    "Spicy Chicken Sandwich & Cheese": {
        "menuID": 1, 
        "itemID": 18,
        "itemAmount": 1
    },
    "Spicy Chicken Sandwich & Sauce": {
        "menuID": 11, 
        "itemID": 24,
        "itemAmount": 1
    },
    "Spicy Chicken Sandwich & Spice": {
        "menuID": 11, 
        "itemID": 25,
        "itemAmount": 1
    },
    "Caeser Salad & Lettuce": {
        "menuID": 12, 
        "itemID": 7,
        "itemAmount": 6
    },
    "Caeser Salad & Cheese": {
        "menuID": 12, 
        "itemID": 18,
        "itemAmount": 1
    },
    "Caeser Salad & Sauce": {
        "menuID": 12, 
        "itemID": 24,
        "itemAmount": 1
    },
    "Caeser Salad & Toast": {
        "menuID": 12, 
        "itemID": 21,
        "itemAmount": 1
    },
    "Ice Cream & Ice Cream": {
        "menuID": 13, 
        "itemID": 16,
        "itemAmount": 2
    },
    "Shakes & Ice Cream": {
        "menuID": 14, 
        "itemID": 16,
        "itemAmount": 2
    },
    "Shakes & Milk": {
        "menuID": 14, 
        "itemID": 26,
        "itemAmount": 2
    },
    "Sundae & Ice Cream": {
        "menuID": 15, 
        "itemID": 16,
        "itemAmount": 2
    },
    "Sundae & Cookies": {
        "menuID": 15, 
        "itemID": 27,
        "itemAmount": 2
    },
    "Float & Ice Cream": {
        "menuID": 16, 
        "itemID": 16,
        "itemAmount": 2
    },
    "Float & Soda": {
        "menuID": 16, 
        "itemID": 29,
        "itemAmount": 2
    },
    "Fries & Potato": {
        "menuID": 17, 
        "itemID": 10,
        "itemAmount": 4
    },
    "Fries & Oil": {
        "menuID": 17, 
        "itemID": 4,
        "itemAmount": 6
    },
    "Fries & Salt": {
        "menuID": 17, 
        "itemID": 5,
        "itemAmount": 6
    },
    "Fries & Ketchup": {
        "menuID": 17, 
        "itemID": 11,
        "itemAmount": 2
    },
    "Small Water & Water Bottle": {
        "menuID": 18, 
        "itemID": 28,
        "itemAmount": 1
    },
    "Large Water & Water Bottle": {
        "menuID": 19, 
        "itemID": 28,
        "itemAmount": 2
    },
    "Pepsi & Soda": {
        "menuID": 20, 
        "itemID": 29,
        "itemAmount": 200
    },
}


# Data for Names
names = ['Zo', 'Cameron', 'Vincent', 'Ryan', 'Jordan', 'Kha'] # Add a lot more names;


# Data for Weekdays and respective working hours
weekday = {
    "Monday" : '11-19',
    "Tuesday" : '10-19',
    "Wednesday" : '10-19',
    "Thursday" : '10-19',
    "Friday" : '10-18',
    "Saturday" : '10-18',
    "Sunday" : '11-18'
}
