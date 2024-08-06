from flask import Flask, request, render_template, redirect, url_for, send_file
import sqlite3
import pandas as pd
import os

app = Flask(__name__)

# Ensure the directory for Excel files exists
EXCEL_PATH = 'static/data.xlsx'

# Database functions
def save_to_db(data, willing):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    email = data[2]
    phone = data[3]

    if willing:
        # Check if the user already exists in the willing_users table
        cursor.execute('SELECT COUNT(*) FROM willing_users WHERE email = ?', (email,))
        exists = cursor.fetchone()[0]
        
        if exists:
            # Update existing record
            cursor.execute('''
                UPDATE willing_users
                SET name=?, department=?, email=?, Phone=?, qualification=?, designation=?, total_experience=?, experience_in_nscet=?, topics=?
                WHERE email=?
            ''', (*data[0:9], email))  # Include all columns
        else:
            # Insert new record
            cursor.execute('''
                INSERT INTO willing_users (name, department, email, Phone, qualification, designation, total_experience, experience_in_nscet, topics)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', data)  # Ensure data has all 9 values
    else:
        # Check if the user already exists in the not_willing_users table
        cursor.execute('SELECT COUNT(*) FROM not_willing_users WHERE email = ?', (email,))
        exists = cursor.fetchone()[0]

        if exists:
            # Update existing record
            cursor.execute('''
                UPDATE not_willing_users
                SET name=?, department=?, email=?, Phone=?, qualification=?, designation=?, total_experience=?, experience_in_nscet=?
                WHERE email=?
            ''', (*data[0:8], phone, email))  # Include phone and email
        else:
            # Insert new record
            cursor.execute('''
                INSERT INTO not_willing_users (name, department, email, Phone, qualification, designation, total_experience, experience_in_nscet)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', data[:8])  # Ensure data has 8 values (excluding Phone)

    conn.commit()
    conn.close()

def export_to_excel():
    conn = sqlite3.connect('database.db')
    df_willing = pd.read_sql_query('SELECT * FROM willing_users ORDER BY timestamp ASC', conn)
    df_not_willing = pd.read_sql_query('SELECT * FROM not_willing_users', conn)

    # Ensure the directory exists
    os.makedirs(os.path.dirname(EXCEL_PATH), exist_ok=True)

    # Export to Excel
    with pd.ExcelWriter(EXCEL_PATH) as writer:
        df_willing.to_excel(writer, sheet_name='Willing Users', index=False)
        df_not_willing.to_excel(writer, sheet_name='Not Willing Users', index=False)

    conn.close()

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        department = request.form['department']
        email = request.form['email']
        phone = request.form.get('phone', '')  # Handle phone number
        qualification = request.form['qualification']
        designation = request.form['designation']
        total_experience = int(request.form['total_experience'])
        experience_in_nscet = int(request.form['experience_in_nscet'])
        topics = ','.join(request.form.getlist('topics'))  # Joining selected topics
        
        willing = 'willing' in request.form

        data = (name, department, email, phone, qualification, designation, total_experience, experience_in_nscet, topics)
        save_to_db(data, willing)

        # Trigger data export to Excel
        export_to_excel()

        return redirect(url_for('success'))

    return render_template('form.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/download')
def download():
    # Serve the Excel file
    return send_file(EXCEL_PATH, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
