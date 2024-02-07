from datetime import datetime, timedelta
from random import randint
from pymongo import MongoClient

mongoURI =  "mongodb+srv://pb_test_user:xQvWQKoM9L6ELtyQ@cluster0.msnrykh.mongodb.net/test_db"
client = MongoClient(mongoURI)
db = client.test_db
collection = db.daily_total_summary


cities = ["Agra", "Delhi", "Bangalore", "Mumbai", "Goa", "Jaipur"]

# Generate sample data for each city
sample_data = []
start_date = datetime(2024, 1, 21)  # Start date for data generation

for city in cities:
    current_date = start_date
    while current_date <= datetime(2024, 2, 4):  # End date for data generation
        data_entry = {
            "city": city,
            "netSale": randint(30000, 50000),
            "netExpense": randint(50000, 70000),
            "dailyTarget": randint(6000000, 9000000),
            "date": current_date.strftime("%Y-%m-%d")
        }
        sample_data.append(data_entry)
        current_date += timedelta(days=1)

# Insert sample data into the collection
collection.insert_many(sample_data)

print("Sample data inserted successfully." )