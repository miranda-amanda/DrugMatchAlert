from flask import Flask, render_template, request, jsonify
import csv
import sqlite3
import os

app = Flask(__name__)
DATABASE = 'data.db'


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def import_csv_to_sqlite():
    if not os.path.exists(DATABASE):
        print("Database not found. Creating and importing data from CSV.")
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('''
            CREATE TABLE combinations (
                drug1 TEXT,
                drug2 TEXT,
                alert TEXT
            )
        ''')
        conn.commit()

        try:
            with open('data.csv', 'r') as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    row = [value.lower() for value in row]
                    print(f"Inserting row: {row}")
                    c.execute('INSERT INTO combinations (drug1, drug2, alert) VALUES (?, ?, ?)', row)
        except Exception as e:
            print(f"Error reading CSV: {e}")

        conn.commit()
        conn.close()
        print("Data imported successfully.")
    else:
        print("Database already exists. Skipping import.")


import_csv_to_sqlite()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_drugs')
def get_drugs():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT DISTINCT drug1 FROM combinations UNION SELECT DISTINCT drug2 FROM combinations")
    drugs = [row[0] for row in c.fetchall()]
    conn.close()
    return jsonify({'drugs': drugs})


@app.route('/verify_combination', methods=['POST'])
def verify_combination():
    drug1 = request.form['drug1'].lower()
    drug2 = request.form['drug2'].lower()

    conn = get_db_connection()
    c = conn.cursor()

    c.execute("SELECT alert FROM combinations WHERE LOWER(drug1)=? AND LOWER(drug2)=?", (drug1, drug2))
    alert = c.fetchone()

    if not alert:
        c.execute("SELECT alert FROM combinations WHERE LOWER(drug1)=? AND LOWER(drug2)=?", (drug2, drug1))
        alert = c.fetchone()

    conn.close()

# I needed the help of ChatGPT at this stage because I couldn't get the buttons to generate the modals.
    if alert:
        color = alert['alert']
        color_class = {'yellow': 'yellow', 'green': 'green', 'red': 'red'}.get(color, 'default')
        return jsonify({'type': 'button', 'content': f'<button class="alert-button {color_class}">{color.capitalize()} Alert</button>'})
    else:
        return jsonify({'type': 'button', 'content': '<button class="alert-button default">Combination not found</button>'})


@app.route('/update_data')
def update_data():
    import_csv_to_sqlite()
    return 'Data updated successfully!'


@app.route('/view_combinations')
def view_combinations():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM combinations")
    combinations = c.fetchall()
    conn.close()
    return render_template('combinations.html', combinations=combinations)


if __name__ == '__main__':
    app.run(debug=True)
