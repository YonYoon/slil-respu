import json
import random
import sqlite3

from flask import Flask, jsonify, render_template

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    # conn.row_factory = sqlite3.Row
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
    return render_template('index.html', quote=quote[0])


@app.route("/get")
def get_random_quote():
    conn = get_db_connection()
    quotes = conn.execute('SELECT * FROM quotes').fetchall()
    conn.close()
    quote = random.choice(quotes)
    json_quote = jsonify(quote)
    return json_quote