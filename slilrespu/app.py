import json
import os
import random
import sqlite3

from flask import Flask, jsonify, render_template

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn

# Function to initialize the database if it doesn't exist
def init_db():
    conn = get_db_connection()
    with app.open_resource('schema.sql', mode='r') as f:
        conn.cursor().executescript(f.read())
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def index():
    json_quote = get_random_quote()
    quote = json.loads(json_quote.data)
    return render_template('index.html', quote=quote)


@app.route("/get")
def get_random_quote():
    conn = get_db_connection()
    quotes = conn.execute('SELECT * FROM quotes').fetchall()
    conn.close()
    quote = random.choice(quotes)
    json_quote = jsonify(quote[1].upper())
    return json_quote


@app.route("/image")
def get_random_image():
    current_directory = os.path.dirname(__file__)
    relative_path = 'static/images/'
    directory = os.path.join(current_directory, relative_path)
    image_names = os.listdir(directory)
    image_name = random.choice(image_names)
    json_name = jsonify(image_name)
    return json_name