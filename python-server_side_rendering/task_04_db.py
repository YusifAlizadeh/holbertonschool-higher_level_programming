from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# --- Functions to read data from sources ---

def read_json(file_path='products.json'):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def read_csv(file_path='products.csv'):
    data = []
    try:
        with open(file_path, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row.get('id', 0))
                row['price'] = float(row.get('price', 0))
                data.append(row)
    except FileNotFoundError:
        pass
    return data

def read_sqlite(db_path='products.db'):
    data = []
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            data.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            })
        conn.close()
    except sqlite3.Error:
        return None
    return data

# --- Flask Route ---
@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    id_param = request.args.get('id')

    # Load data based on source
    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        data = read_sqlite()
        if data is None:
            return render_template('product_display.html', error="Database error", products=[])
    else:
        return render_template('product_display.html', error="Wrong source", products=[])

    # Filter by id if provided
    if id_param:
        try:
            id_value = int(id_param)
            filtered = [item for item in data if item.get('id') == id_value]
            if not filtered:
                return render_template('product_display.html', error="Product not found", products=[])
            data = filtered
        except ValueError:
            return render_template('product_display.html', error="Invalid id", products=[])

    return render_template('product_display.html', products=data, error=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
