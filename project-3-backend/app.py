import requests
import json
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, select
import os
from dotenv import load_dotenv
from flask_cors import CORS
from datetime import datetime
import deepl
from collections import defaultdict

app = Flask(__name__)
CORS(app)
load_dotenv()

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('PSQL_USER')}:{os.getenv('PSQL_PASSWORD')}@{os.getenv('PSQL_HOST')}/{os.getenv('PSQL_DATABASE')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

###################################
#             Employee API        #
###################################
@app.route('/api/employee/<name>')
def get_data(name):
    query = text("SELECT * FROM Employees WHERE employeename = :name LIMIT 1")
    result = db.session.execute(query, {'name': name}).fetchone()

    if result is not None:
        data = {'employeename': result.employeename, 'position': result.position}
        return jsonify(data)
    else:
        return jsonify({'error': 'No data found'}), 404

###################################
#             MENU API            #
###################################
@app.route('/api/menu', methods=['GET', 'POST'])
def get_menu_items():
    if request.method == 'GET':
        query = text("SELECT * FROM Menu ORDER BY itemName ASC")
        results = db.session.execute(query).fetchall() 
        if results:
            data = []
            if 'translate' in request.args and request.args.get("translate") != 'EN':
                texts = []
                for row in results:
                    texts.append(str(row[1]))
                names = translator.translate_text(text=texts, target_lang=request.args.get("translate"))
                for i, row in enumerate(results):
                    item = {
                        'id' : row[0],
                        'itemName' : names[i].text,
                        'price' : row[2]
                    }
                    data.append(item)
            else:
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
    elif request.method == 'POST':
        data = request.get_json()
        res = db.session.execute(text("SELECT MAX(id) FROM Menu")).fetchone()[0] + 1
        query = text("INSERT INTO menu (id, itemname, price) VALUES (:id, :itemName, :price);")
        db.session.execute(query, {'id': res, 'itemName': data['itemName'], 'price': data['price']})
        db.session.commit()
        return jsonify({'message': 'Menu item created successfully'}), 201
    
@app.route('/api/menu/<menu_id>', methods=['PUT', 'DELETE'])
def get_menu_item(menu_id):
    if request.method == 'PUT':
        data = request.get_json()
        # print(data)
        query = text("UPDATE Menu SET itemName = :itemName, price = :price WHERE id = :id")
        db.session.execute(query, {'itemName': data['itemName'], 'price': data['price'], 'id': menu_id})
        db.session.commit()
        return jsonify({'message': 'Menu item updated successfully'}), 200
    elif request.method == 'DELETE':
        delete_menu_mijunc_batch(menu_id)
        delete_menu_omjunc_batch(menu_id)
        query = text("DELETE FROM Menu WHERE id = :id")
        db.session.execute(query, {'id': menu_id})
        db.session.commit()
        return jsonify({'message': 'Menu item deleted successfully'}), 200
    
def delete_menu_omjunc_batch(menu_id):
    try:
        query = text("DELETE FROM OMJunc WHERE menuid = :menu_id")
        db.session.execute(query, {'menu_id': menu_id})
        db.session.commit()
        return jsonify({'message': 'Menu order deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': 'Issue with deletion' + e}), 404

#Deleting all inventory items attached to the menu item
def delete_menu_mijunc_batch(menu_id):
    try:
        query = text("DELETE FROM MIJunc WHERE menuid = :menu_id")
        db.session.execute(query, {'menu_id': menu_id})
        db.session.commit()
        return jsonify({'message': 'Menu inventory deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': 'Issue with deletion' + e}), 404

###################################
#             Inventory API       #
###################################
@app.route('/api/inventory')
def get_inventory_items():
    query = text("SELECT * FROM Inventory ORDER BY name ASC")
    results = db.session.execute(query).fetchall()
    if results:
        data = []
        for row in results:
            item = {
                'id' : row[0],
                'name' : row[1],
                'stock' : row[2],
                'location' : row[3],
                'capacity' : row[4],
                'supplier' : row[5],
                'minimum' : row[6]
            }
            data.append(item)

        return jsonify(data)
    else:
        return jsonify({'error': 'No data found'}), 404

# GET: Find all low stock items
@app.route('/api/inventory/shortage', methods=['GET'])
def get_inventory_shortage():
    query = text("SELECT * FROM Inventory WHERE stock < minimum ORDER BY name ASC")
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

@app.route('/api/inventory/<inventory_id>', methods=['PUT', "GET"])
def update_inventory(inventory_id):
    if request.method == 'GET':
        data = []
        if(inventory_id.isnumeric() == False):
            query = text("SELECT id FROM Inventory WHERE name = :name")
            result = db.session.execute(query, {'name': inventory_id}).fetchone()
            
        else:
            query = text("SELECT * FROM Inventory WHERE id = :id")
            result = db.session.execute(query, {'id': inventory_id}).fetchone()
        if result is not None:
            return jsonify({
                'id' : result.id,
                'name' : result.name,
                'stock' : result.stock,
                'location' : result.location,
                'supplier' : result.supplier,
                'minimum' : result.minimum
            })
        else:
            return jsonify({'error': 'No data found'}), 404
    elif(request.method == 'PUT'):
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
    elif(request.method == 'DELETE'):
        query = text("DELETE FROM Inventory WHERE id = :id")
        db.session.execute(query, {'id': inventory_id})
        db.session.commit()
        return jsonify({'message': 'Inventory item deleted successfully'}), 200

def update_inventory_batch(data):
    query = text("UPDATE Inventory SET stock = stock + :add_stock WHERE id = :id")
    params = [{'add_stock': item['amount'], 'id': item['id']} for item in data]
    db.session.execute(query, params)
    db.session.commit()

###################################
#             MIJUNC API          #
###################################
@app.route('/api/mijunc/<menu_id>', methods=['GET', 'DELETE', 'POST', 'PUT'])
def get_menu_inventory(menu_id):
    if(request.method == 'GET'):
        query = text("SELECT m.itemid, i.name, m.itemamount FROM mijunc as m JOIN Inventory as i On m.itemid = i.id WHERE menuid = :menu_id  ORDER BY i.name ASC")
        try:
            results = db.session.execute(query, {'menu_id': menu_id}).fetchall()
            data = []
            # print(results)
            for row in results:
                item = {
                    'itemID' : row.itemid,
                    'itemName' : row.name,
                    'itemAmount' : row.itemamount
                }
                data.append(item)

            return jsonify(data)
        except Exception as e:
            return jsonify({'error': 'No data found' + e}), 404
    elif(request.method == 'DELETE'):
        data = request.get_json()
        query = text("DELETE FROM MIJunc WHERE menuid = :menu_id AND itemid = :item_id")
        db.session.execute(query, {'menu_id': menu_id, 'item_id': data['itemID']})
        db.session.commit()
        return jsonify({'message': 'Menu inventory deleted successfully'}), 200
    elif request.method == 'POST':
        data = request.get_json()
        query = text("INSERT INTO MIJunc (menuID, itemID, itemAmount) VALUES (:menu_id, :item_id, :item_amount)")
        db.session.execute(query, {'menu_id': menu_id, 'item_id': data['itemID'], 'item_amount': data['itemAmount']})
        db.session.commit()
        return jsonify({'message': 'Menu inventory created successfully'}), 201
    elif request.method == 'PUT':
        data = request.get_json()
        query = text("UPDATE MIJunc SET itemAmount = :item_amount WHERE menuID = :menu_id AND itemID = :item_id")
        db.session.execute(query, {'item_amount': data['itemAmount'], 'menu_id': menu_id, 'item_id': data['itemID']})
        db.session.commit()
        return jsonify({'message': 'Menu inventory updated successfully'}), 200

#Needed to get all the inventory items that are not in the list of a menu item
@app.route('/api/mijunc/outside/<menu_id>', methods=['GET'])
def get_outside_menu_inventory(menu_id):
    query = text("SELECT DISTINCT inv.id, inv.name FROM Inventory as inv WHERE inv.id NOT IN (SELECT i.id FROM mijunc as m JOIN Inventory as i On m.itemid = i.id WHERE menuid = :menu_id) ORDER BY inv.name ASC")
    try:
        results = db.session.execute(query, {'menu_id': menu_id}).fetchall()
        data = []
        # print(results)
        for row in results:
            item = {
                'itemID' : row.id,
                'itemName' : row.name,
            }
            data.append(item)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': 'No data found' + e}), 404


###################################
#             Ordering API        #
###################################
@app.route('/api/order', methods=['POST', 'GET'])
def update_orders():
    if(request.method == 'POST'):
        data = request.get_json() #turns the JSON into a python dict

        # Insert order
        curr_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
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
    
    elif request.method == 'GET':
        try:
            data = request.json()
            #START AND END TIME NEED TO BE IN THE FORMAT 'YYYY-MM-DD HH:MM:SS'
            query = text("SELECT * FROM Orders WHERE time BETWEEN :start_time AND :end_time LIMIT 100")
            results = db.session.execute(query, {'start_time': data['start_time'], 'end_time': data['end_time']}).fetchall()
            data = []
            for row in results:
                item = {
                    'id' : row.id,
                    'customerName' : row.customername,
                    'time' : row.time,
                    'paid' : row.paid,
                    'employeeID' : row.employeeid
                }
                data.append(item)
            return jsonify(data)
        except Exception as e:
            return jsonify({'error': 'No data found' + e}), 404

@app.route('/api/order/<order_id>', methods=['DELETE'])
def delete_order(order_id):
    #Deletes the order menu junction
    delete_order_omjunc_batch(order_id)
    
    #Deletes the order
    query = text("DELETE FROM Orders WHERE id = :order_id")
    db.session.execute(query, {'order_id': order_id})
    db.session.commit()
    return jsonify({'message': 'Order deleted successfully'}), 200

def delete_order_omjunc_batch(order_id):
    try:
        query = text("DELETE FROM OMJunc WHERE orderid = :order_id")
        db.session.execute(query, {'order_id': order_id})
        db.session.commit()
        return jsonify({'message': 'Order menu deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': 'Issue with deletion' + e}), 404

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
Returns menu id : number of times ordered
'''
@app.route('/api/sales_by_time')
def sales_by_time():
    # Parse start_time and end_time from request arguments
    start_time = request.args.get('start_time')  # e.g., '2023-01-01 00:00:00'
    end_time = request.args.get('end_time')  # e.g., '2023-01-02 23:59:59'

    # Adjust SQL to count occurrences of each menuID
    sql = text("""
        SELECT M.itemName, OM.menuID, COUNT(*) as frequency FROM Orders O
        JOIN OMJunc OM ON O.id = OM.orderID
        JOIN menu M ON M.id = OM.menuID
        WHERE O.time >= :start_time AND O.time <= :end_time
        GROUP BY M.itemName, OM.menuID
        ORDER BY OM.menuID;
    """)

    # Execute query with bound parameters
    result = db.session.execute(sql, {'start_time': start_time, 'end_time': end_time}).fetchall()
    # print(result)

    # Process result into a dictionary {menuID: frequency}
    
    menu_sales_data = [{'menuName': row[0], 'menuID': row[1], 'frequency': row[2]} for row in result]

    # Return JSON response
    return jsonify(menu_sales_data)

# Returns excess menu ids
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
    # Adjusted for direct access without assuming dictionary-like access
    sql_inventory = text("SELECT id, stock FROM Inventory;")
    inventory_result = db.session.execute(sql_inventory).fetchall()
    excess_item_ids = [row.id for row in inventory_result if item_amount_map.get(row.id, 0) * 10 < row.stock]
    # Generate menuIDs for the identified excess items
    if excess_item_ids:
        # This step requires dynamically generating SQL, be cautious of SQL injection
        excess_item_ids_str = ', '.join(str(item_id) for item_id in excess_item_ids)
        sql_menu_ids = text(f"""
            SELECT DISTINCT MI.menuID, M.itemName
            FROM MIJunc MI
            JOIN MENU M ON MI.menuID = M.id
            WHERE MI.itemID IN ({excess_item_ids_str})
        """)
        menu_ids_result = db.session.execute(sql_menu_ids).fetchall()
        menu_ids_result.sort()
        menu_data = [{'menuID': row[0], 'menuName': row[1]} for row in menu_ids_result]
    else:
        menu_data = []

    return jsonify(menu_data)


@app.route('/api/order_history')
def order_history():
    # Get the query parameter for sorting order; default is descending
    ascending = request.args.get('ascending', 'false').lower() == 'true'
    
    time_clause = ""
    
    # Parse start_time and end_time from request arguments
    if 'start_time' in request.args and 'end_time' in request.args:
        start_time = request.args.get('start_time', default='')  # e.g., '2023-01-01 00:00:00'
        end_time = request.args.get('end_time')  # e.g., '2023-01-02 23:59:59'
        time_clause = f"WHERE Orders.time BETWEEN '{start_time}' AND '{end_time}'"
    
    order_by_clause = "ORDER BY Orders.id ASC" if ascending else "ORDER BY Orders.id DESC"
    sql_stmt = text(f"""
        SELECT 
            OMJunc.orderID, 
            Menu.itemName, 
            Menu.price, 
            Orders.customerName, 
            Orders.EmployeeID
        FROM 
            OMJunc
        INNER JOIN 
            Menu ON OMJunc.menuID = Menu.id
        INNER JOIN
            Orders ON OMJunc.orderID = Orders.id
        {time_clause}
        {order_by_clause}
        LIMIT 
            300;
    """)
    
    result = db.session.execute(sql_stmt).fetchall()
    # print(result)

    # Use a dictionary to aggregate orders
    orders = defaultdict(lambda: {
        'customerName': '',
        'employeeID': None,
        'items': [],
        'totalPrice': 0.0
    })

    # Process each row in the result
    for row in result:
        order_id = row[0]
        order = orders[order_id]
        order['customerName'] = row[3]
        order['employeeID'] = row[4]
        order['items'].append({
            'itemName': row[1],
            'price': float(row[2])
        })
        order['totalPrice'] += float(row[2])

    # Convert aggregated orders into a list
    data = [{
        'orderID': order_id,
        'customerName': info['customerName'],
        'employeeID': info['employeeID'],
        'items': info['items'],
        'totalPrice': round(info['totalPrice'], 2)  # Round total price to 2 decimal places
    } for order_id, info in orders.items()]

    return jsonify(data)


@app.route('/api/product_usage')
def product_usage_report():
    # Parse start_time and end_time from request arguments
    start_time = request.args.get('start_time')  # e.g., '2023-01-01 00:00:00'
    end_time = request.args.get('end_time')  # e.g., '2023-01-02 23:59:59'

    sql_stmt = text("SELECT I.name, SUM(MI.itemAmount) as sumAmount FROM OMJunc OM "
                        + "JOIN MIJunc MI ON OM.menuID = MI.menuID "
                        + "JOIN Orders O ON OM.orderID = O.id " 
                        + "JOIN Inventory I ON MI.itemID = I.id "
                        + "WHERE O.time >= :start_time AND O.time <= :end_time "
                        + "GROUP BY I.name;")
    
    result = db.session.execute(sql_stmt, {'start_time': start_time, 'end_time': end_time}).fetchall()
    # print(result)

    total_amount = sum(row[1] for row in result)

    # Process result into a dictionary {name: quantity, percentage}
    menu_names_list = {row[0]: {'amount': row[1], 'percentage': round((row[1] / total_amount * 100), 2)} for row in result}
    
    return jsonify(menu_names_list)

@app.route('/api/sells_together')
def what_sells_together():
    # Parse start_time and end_time from request arguments
    start_time = request.args.get('start_time')  # e.g., '2023-01-01 00:00:00'
    end_time = request.args.get('end_time')  # e.g., '2023-01-02 23:59:59'

    sql_stmt = text("SELECT O.id, M.itemName FROM Orders O "
                        + "JOIN OMJunc OM ON O.id = OM.orderID "
                        + "JOIN Menu M ON OM.menuID = M.id "
                        + "WHERE O.time >= :start_time AND O.time <= :end_time ORDER BY O.time;")
        
    result = db.session.execute(sql_stmt, {'start_time': start_time, 'end_time': end_time}).fetchall()
        

    menu_items_by_order_id = {}

    for row in result:
        order_id = row[0]
        menu_item = row[1]

        if order_id in menu_items_by_order_id:
            menu_items_by_order_id[order_id].append(menu_item)
        else:
            menu_items_by_order_id[order_id] = [menu_item]

    pair_frequency = {}

    for order_id, menu_items in menu_items_by_order_id.items():
        menu_items.sort()
        for i in range(len(menu_items)):
            for j in range(i + 1, len(menu_items)):
                if menu_items[i] == menu_items[j]:
                    continue
                inner_dict = pair_frequency.setdefault(menu_items[i], {})
                inner_dict[menu_items[j]] = inner_dict.get(menu_items[j], 0) + 1
                pair_frequency[menu_items[i]] = inner_dict
    
    pair_item_list = []
    for name1, inner_map in pair_frequency.items():
        for name2, frequency in inner_map.items():
            pair_with_frequency = [name1, name2, frequency]
            pair_item_list.append(pair_with_frequency)

    pair_item_list.sort(key=lambda x: x[2], reverse=True)
                        
    return jsonify(pair_item_list)
    
    
auth_key = os.getenv('DEEPL_API_KEY')
translator = deepl.Translator(auth_key)
class Language:
    def __init__(self, name, code):
        self.code = code
        self.name = name
    
    def getName(self):
        return self.name
    
    def getCode(self):
        return self.code

# target_lang = Language('English', 'EN')

@app.route('/api/translate', methods=['POST', 'GET'])
def translate_route():
    if request.method == 'GET':
        data = []
        for lang in translator.get_source_languages():
            item = {
                'name' : lang.name,
                'code' : lang.code
            }
            data.append(item)
        return jsonify(data), 200
    elif request.method == 'POST':
        try:
            data = request.get_json()
            if isinstance(data['text'], list):
                texts = data['text']
                res_lang = data['target_language']
                if res_lang == 'EN':
                    res_lang = 'EN-US'
                transformed_text = translator.translate_text(text=texts, target_lang=res_lang)
                return jsonify({'translated_text': transformed_text.text}), 200
            else:
                text = data['text']
                res_lang = data['target_language']
                transformed_text = translator.translate_text(text=text, target_lang=res_lang)
                print("Transformed Text", transformed_text.text, res_lang)
                return jsonify({'translated_text': transformed_text.text}), 200
        except Exception as e:
            print("Bad Request", e)
            return jsonify({'error': 'Translation failed'}), 404

# @app.route('/api/translate/language', methods=['POST'])
# def translate_language():
#     data = request.get_json()
#     target_lang.code = data['language']
#     print(target_lang.code)
#     return jsonify({'message': 'Language set successfully'})

if __name__ == '__main__':
    app.run(debug=True)
