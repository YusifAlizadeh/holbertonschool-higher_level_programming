from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# Function to read JSON data
def read_json(file_path='products.json'):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Function to read CSV data
def read_csv(file_path='products.csv'):
    data = []
    try:
        with open(file_path, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert id to int and price to float
                row['id'] = int(row.get('id', 0))
                row['price'] = float(row.get('price', 0))
                data.append(row)
    except FileNotFoundError:
        pass
    return data

@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    id_param = request.args.get('id')

    # Load data based on source
    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
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
