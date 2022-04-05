from flask import Flask, request, jsonify,render_template
from sql_connection import get_sql_connection
import mysql.connector
import json

import products_dao
import orders_dao
import uom_dao

app = Flask(__name__)

connection = get_sql_connection()

@app.route('/', methods=['GET'])
def showIndex():
    return render_template('index.html')

@app.route('/product', methods=['GET'])
def showProduct():
    return render_template('manage-product.html')

@app.route('/order', methods=['GET'])
def showOrder():
    return render_template('order.html')

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)

