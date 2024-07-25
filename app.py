from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/CrudApp'
mongo = PyMongo(app)
CORS(app)

db = mongo.db.users

@app.route('/')
def index():
    return '<h1>Hello world1</h1>'

@app.route('/api/users', methods=['POST'])
def create_user():
    user = {
        'name': request.json['name'],
        'email': request.json['email'],
        'contact': request.json['contact'],
        'address': request.json['address']
    }
    db.insert_one(user)
    return jsonify(str(user))

@app.route('/api/users', methods=['GET'])
def get_users():
    users = []
    for doc in db.find():
        users.append({
            '_id': str(doc['_id']),
            'name': doc['name'],
            'email': doc['email'],
            'contact': doc['contact'],
            'address': doc['address']
        })
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
