import sqlite3

def create_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create willing_users table
    # Remove the UNIQUE constraint on the Phone column
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS willing_users_temp AS
    SELECT * FROM willing_users
''')
    cursor.execute('DROP TABLE willing_users')
    cursor.execute('''
    CREATE TABLE willing_users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        Phone NUMBER,
        qualification TEXT,
        designation TEXT,
        total_experience INTEGER,
        experience_in_nscet INTEGER,
        topics TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')
    cursor.execute('''
    INSERT INTO willing_users (id, name, department, email, Phone, qualification, designation, total_experience, experience_in_nscet, topics, timestamp)
    SELECT id, name, department, email, Phone, qualification, designation, total_experience, experience_in_nscet, topics, timestamp
    FROM willing_users_temp
''')
    cursor.execute('DROP TABLE willing_users_temp')


    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()
