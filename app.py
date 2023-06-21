import os
from flask import Flask, jsonify, request
from firebase_admin import credentials, initialize_app, db

app = Flask(__name__)

cred = credentials.Certificate('./accounts/pythonfire-38361-firebase-adminsdk-yhjo4-6526107e5c.json')
firebase_app = initialize_app(cred,{
    'databaseURL':'https://<your database>.firebasedatabase.app/'
})

rdb = db.reference()
@app.route('/todos', methods=['GET'])
def get_todos():
    todos = rdb.child('todos').get()
    return jsonify({'todos':todos})

@app.route('/todos', methods=['POST'])
def create_todo():
    todo = request.json['todo']
    todo_ref = rdb.child('todos').push(todo)
    return jsonify({'id':todo_ref.key, 'todo':todo})

if __name__ == '__main__':
    app.run(debug=True)