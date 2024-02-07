from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime , timedelta


app = Flask(__name__)
CORS(app)

#Connection to mongodb

mongoURI =  "mongodb+srv://pb_test_user:xQvWQKoM9L6ELtyQ@cluster0.msnrykh.mongodb.net/test_db"
client = MongoClient(mongoURI)
db = client.test_db
collection = db.daily_total_summary





# DEfining Endpoints for the API

@app.route('/data', methods=['GET'])
def get_data():
    try:
        city = request.args.get('city')
        if not city or city not in ["Agra", "Delhi", "Banglore", "Bombay", "Goa", "Jaipur"]:
            return jsonify({'code': 400, 'status': 'Error', 'message': 'Invalid city parameter'}), 400

        end_date = datetime(2024, 2, 5)
        start_date = end_date - timedelta(days=15)
        date= []
        for i in range(15):
            date.append((end_date - timedelta(days=i)).strftime("%Y-%m-%d"))
        data = list(collection.find({
            'city': city,
            'date': {'$in': date}
        }, {'_id': 0}))

        
        
        
        return jsonify(message="Success", data=data)
        
    except Exception as e:
        return jsonify(message="Error", error=str(e))



if __name__ == '__main__':
    app.run(debug=True)

