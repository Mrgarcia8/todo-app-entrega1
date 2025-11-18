from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/tasks')
def tasks():
    return jsonify({'message': 'API funcionando correctamente'})

app.run(host='0.0.0.0', port=5000)
