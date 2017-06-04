#!/usr/bin/env python

from flask import Flask, jsonify
from pymongo import MongoClient
from flask_pymongo import PyMongo
from flask import request
import os

#client = MongoClient()
#client = MongoClient('localhost', 27017)
#mydb = client.TheHapps



app = Flask(__name__)

app.config['MONGO_DBNAME']='TheHapps'
app.config['MONGO_URI']="ds163181.mlab.com"
app.config['MONGO_PORT']="63181"
app.config['MONGO_USERNAME']="heroku_q3r859wz"
app.config['MONGO_URI']="t86dtebektbren389fktmqo8mi"
mongo=PyMongo(app)


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})
	

@app.route('/event', methods=['GET'])
def get_all():
	Event=mongo.db.Event
	
	output=[]
	for q in Event.find(): 
		output.append({'Event':q['Name'],'Description':q['Description']})
	
	return jsonify(output)

@app.route('/event/<name>', methods=['GET'])
def get_one(name):
	Event=mongo.db.Event
	print(Event)
	q=Event.find_one({'Name':name})
	if q:
		output={'Name':q['Name'],'Description':q['Description']}
	else:
		output="No results found"
	return jsonify(output)	

	
@app.route('/event', methods=['POST'])
def post_one():
	Event=mongo.db.Event
	Name_req  =request.json['Name']
	Description_req = request.json['Description']
	
	event_insert=Event.insert({'Name':Name_req,'Description':Description_req})
	q=Event.find_one({'Name':Name_req})
	output={'Name':q['Name'],'Description':q['Description'],'Message':'Successfully inserted'}
	return jsonify(output)	
	
	
	Event=mongo.db.Event
	print(Event)
	q=Event.find_one({'Name':name})
	if q:
		output={'Name':q['Name'],'Description':q['Description']}
	else:
		output="No results found"
	return jsonify(output)	
	
	
if __name__ == '__main__':
    #app.run(debug=True)
	
	port = int(os.environ.get('PORT', 5300))
	app.run(host='0.0.0.0', port=port, debug=True)