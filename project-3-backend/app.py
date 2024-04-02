import requests
import json
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, select
import os
from dotenv import load_dotenv
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": os.getenv('FRONTEND_URL')}})
load_dotenv()

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('PSQL_USER')}:{os.getenv('PSQL_PASSWORD')}@{os.getenv('PSQL_HOST')}/{os.getenv('PSQL_DATABASE')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/employee/<name>')
def get_data(name):
    query = text("SELECT * FROM Employees WHERE employeename = :name LIMIT 1")
    result = db.session.execute(query, {'name': name}).fetchone()

    if result is not None:
        data = {'employeename': result.employeename, 'position': result.position}
        return jsonify(data)
    else:
        return jsonify({'error': 'No data found'}), 404

@app.route('/api/menu')
def get_menu_items():
    query = text("SELECT * FROM Menu")
    results = db.session.execute(query).fetchall() 
    if results:
        data = []
        for row in results:
            item = {
                'id' : row[0],
                'itemName' : row[1],
                'price' : row[2]
            }
            data.append(item)

        return jsonify(data)
    else:
        return jsonify({'error': 'No data found'}), 404
    
@app.route('/api/inventory')
def get_inventory_items():
    query = text("SELECT name, stock, location, capacity, supplier, minimum FROM Inventory")
    results = db.session.execute(query).fetchall()
    if results:
        data = []
        for row in results:
            item = {
                'name' : row[0],
                'stock' : row[1],
                'location' : row[2],
                'capacity' : row[3],
                'supplier' : row[4],
                'minimum' : row[5]
            }
            data.append(item)

        return jsonify(data)
    else:
        return jsonify({'error': 'No data found'}), 404

# GET: Find all low stock items
@app.route('/api/inventory/shortage', methods=['GET'])
def get_inventory_shortage():
    query = text("SELECT * FROM Inventory WHERE stock < minimum;")
    results = db.session.execute(query).fetchall()
    if results:
        data = []
        for row in results:
            item = {
                'id' : row.id,
                'name' : row.name,
                'stock' : row.stock,
                'location' : row.location,
                'supplier' : row.supplier,
                'minimum' : row.minimum
            }
            data.append(item)
        print("Returned all stock shortage items")
        return jsonify(data)
    else:
        return jsonify({'error': 'No data found'}), 404

@app.route('/api/inventory/<inventory_id>', methods=['PUT'])
def update_inventory(inventory_id):
    if(request.method == 'PUT'):
        if(inventory_id.isnumeric() == False):
            query = text("SELECT id FROM Inventory WHERE name = :name")
            result = db.session.execute(query, {'name': inventory_id}).fetchone()
            if result is not None:
                inventory_id = result[0]
            else:
                return jsonify({'error': 'No data found'}), 404
        data = request.get_json()
        query = text("UPDATE Inventory SET stock = stock + :add_stock WHERE id = :id")
        db.session.execute(query, {'add_stock': data['add_stock'], 'id': inventory_id})
        print('Updated stock for item with ID: ' + str(inventory_id))
        db.session.commit()
        return jsonify({'message': 'Stock updated successfully'}), 200

def update_inventory_batch(data):
    query = text("UPDATE Inventory SET stock = stock + :add_stock WHERE id = :id")
    params = [{'add_stock': item['amount'], 'id': item['id']} for item in data]
    db.session.execute(query, params)
    db.session.commit()

@app.route('/api/order', methods=['POST'])
def update_orders():
    if(request.method == 'POST'):
        data = request.get_json() #turns the JSON into a python dict

        # Insert order
        curr_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = text("INSERT INTO orders (customerName, time, paid, EmployeeID) VALUES (:customer_name, :time, :paid, :employee_id);")
        db.session.execute(query, {'customer_name': data['customer_name'], 'time': curr_time, 'paid': data['paid'], 'employee_id': data['employee_id']})
        
        # Get the order id
        query = text("SELECT * FROM orders WHERE :customer_name = customerName AND :time = time AND :paid = paid AND :employee_id = EmployeeID")
        order_id = db.session.execute(query, {'customer_name': data['customer_name'], 'time': curr_time, 'paid': data['paid'], 'employee_id': data['employee_id']}).fetchone()[0]
        print('Inserted order for customer: ' + data['customer_name'] + " successfully with ID: " + str(order_id))
        
        # Insert order menu items
        for menu_id in data['menu_items']:
            query = text("INSERT INTO OMJunc (menuID, orderID) VALUES (:menu_id, :order_id)")
            db.session.execute(query, {'menu_id': menu_id, 'order_id': order_id})

        # Decreasing the stock from the menu items
        query = text("SELECT itemID, itemAmount FROM MIJunc WHERE menuID IN :menu_items")
        results = db.session.execute(query, {'menu_items': tuple(data['menu_items'])}).fetchall() #Returns it in the form of (itemID, itemAmount)
        data = []
        for inventory in results:
            data.append({ "id": inventory[0], "amount": float(-inventory[1]) })
        if data is not None:
            update_inventory_batch(data)
            print('Decreased stock for menu item with ID: ' + str(menu_id))

        db.session.commit()
        return jsonify({'message': 'Order created successfully'}), 201
    
@app.route('/api/weather')
def show_Weather():
    api_key = os.getenv('weather_api_key')
    city_name = "College Station"
    Weather_URL = "http://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=" + api_key
    
    response = requests.get(Weather_URL)
    weather_info = response.json()

    if weather_info['cod'] == 200:
        kelvin = 273
        temp_k = weather_info['main']['temp']
        description = weather_info['weather'][0]['description']
        
        # Convert temperatures from Kelvin to Fahrenheit
        temp_f = (temp_k - kelvin) * 9/5 + 32
        
        # Construct the response JSON object
        result = {
            "temperature_fahrenheit": round(temp_f, 2),
            "description": description
        }
    else:
        result = {
            "error": "Weather not found. COD was not 200"
        }

    return jsonify(result)


'''
Usage: /api/sales_by_time?start_time=2023-01-01%2000:00:00&end_time=2023-01-01%2023:59:59
%20 is used as a space in the URL so, the above start time is: 2023-01-01 00:00:00
End time is: 2023-01-01 23:59:59
'''
@app.route('/api/sales_by_time')
def sales_by_time():
    # Parse start_time and end_time from request arguments
    start_time = request.args.get('start_time')  # e.g., '2023-01-01 00:00:00'
    end_time = request.args.get('end_time')  # e.g., '2023-01-02 23:59:59'

    # Adjust SQL to count occurrences of each menuID
    sql = text("""
        SELECT OM.menuID, COUNT(*) as frequency FROM Orders O
        JOIN OMJunc OM ON O.id = OM.orderID
        WHERE O.time >= :start_time AND O.time <= :end_time
        GROUP BY OM.menuID
        ORDER BY OM.menuID;
    """)

    # Execute query with bound parameters
    result = db.session.execute(sql, {'start_time': start_time, 'end_time': end_time}).fetchall()
    print(result)

    # Process result into a dictionary {menuID: frequency}
    menu_id_frequencies = {row[0]: row[1] for row in result}

    # Return JSON response
    return jsonify(menu_id_frequencies)

@app.route('/api/excess_report')
def excess_report():
    start_time = request.args.get('start_time')  # Example format: '2023-01-01 00:00:00'
    end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    sql_stmt = text("""
        SELECT MI.itemID, SUM(MI.itemAmount) AS sumAmount
        FROM OMJunc OM
        JOIN MIJunc MI ON OM.menuID = MI.menuID
        JOIN Orders O ON OM.orderID = O.id
        WHERE O.time >= :start_time AND O.time <= :end_time
        GROUP BY MI.itemID
    """)

    result = db.session.execute(sql_stmt, {'start_time': start_time, 'end_time': end_time}).fetchall()
    if result:
        data = []
        for row in result:
            item = {
                'id' : row[0],
                'Amount' : row[1],
            }
            data.append(item)
    item_amount_map = {row[0]: row[1] for row in result}
    print('ITEM AMOUNT MAP', item_amount_map)
    # Adjusted for direct access without assuming dictionary-like access
    sql_inventory = text("SELECT id, stock FROM Inventory;")
    inventory_result = db.session.execute(sql_inventory).fetchall()
    excess_item_ids = [row.id for row in inventory_result if item_amount_map.get(row.id, 0) * 10 < row.stock]
    print('EXCESS items:', excess_item_ids)
    # Generate menuIDs for the identified excess items
    if excess_item_ids:
        # This step requires dynamically generating SQL, be cautious of SQL injection
        excess_item_ids_str = ', '.join(str(item_id) for item_id in excess_item_ids)
        print('Excess_item_ids in string', excess_item_ids_str)
        sql_TEST = text(f"SELECT menuID FROM MIJunc WHERE itemID = 12;")
        sql_TEST_result = db.session.execute(sql_TEST).fetchall()
        print('SQL TEST:', sql_TEST_result)

        sql_menu_ids = text(f"SELECT menuID FROM MIJunc WHERE itemID IN ({excess_item_ids_str});") #Issue here
        menu_ids_result = db.session.execute(sql_menu_ids).fetchall()
        print('Menu_ids_result:', menu_ids_result) #why is this blank
        menu_ids_list = [row.menuID for row in menu_ids_result]
        print('Menu IDS LIST:', menu_ids_list)
        print('Should be returned')
    else:
        print('Cooked')
        menu_ids_list = []

    return jsonify(menu_ids_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
