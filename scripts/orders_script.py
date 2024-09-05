import csv
import random
from datetime import datetime, timedelta
from data_script import menu, names, weekday

def generate_order_csv(order_csv_path, omjunc_csv_path, num_days=365):
    
    #100 orders for testing, will use 100,000 for deployment
    num_of_orders = 100
    time = datetime(2024, 2, 20, 10) # Set the starting time to Rev's Start time, for Tuesday

    num_of_orders = 100
    order_number = 1
    junc_ids = 1

    with open(omjunc_csv_path, mode = 'w', newline = '') as omjunc_file, \
        open(order_csv_path, mode = 'w', newline = '') as order_file:

        omjunc_writer = csv.writer(omjunc_file)
        order_writer = csv.writer(order_file)

        for day in range(1, num_days + 1):
            
            minimum_per_day = 3000
            dt1 = datetime(2024, 8, 24)
            dt2 = datetime(2025, 1, 10)
            day1, month1, year1 = dt1.day, dt1.month, dt1.year
            day2, month2, year2 = dt2.day, dt2.month, dt2.year

            if ((day1 == time.day and month1 == time.month and year1 == time.year) or (day2 == time.day and month2 == time.month and year2 == time.year)):
                minimum_per_day = 7000

            minimum_per_day += random.randint(0, 500)
            total_order_price = 0

            while total_order_price < minimum_per_day: 
                # Sets up the ordering history
                order_size = random.randint(1, 5)
                order_total_paid = 0

                # Generates every single order for the entire day
                for order in range(order_size):
                    menu_keys = list(menu.keys())
                    item = random.choice(menu_keys)
                    price = menu[item]
                    total_order_price += price
                    order_total_paid += price

                    #insert into OMJunc with order_number and item
                    # Write a new row to the CSV file
                    omjunc_writer.writerow([junc_ids, int(item[:2]), order_number])
                    junc_ids += 1

                minute_delta = 0
                second_delta = 0
                if minimum_per_day >= 7000:
                    minute_delta = 0
                    second_delta = random.randint(15, 70)
                else:
                    minute_delta = random.randint(1, 2)
                    second_delta = random.randint(1, 59)
                time = time + timedelta(minutes = minute_delta, seconds= second_delta)
                
                # Inserts the orders into the database
                name = random.choice(names)
                rand_employeeID = random.choice([2, 4, 6])

                # Write a new row to the CSV file
                order_writer.writerow([order_number, name, time, f"{order_total_paid:.2f}", rand_employeeID])

                order_number += 1

            # Resets the time to the next day after all orders
            time += timedelta(days=1)
            time = time.replace(hour = int(weekday[time.strftime("%A")][:2]), minute = 0, second=0)
