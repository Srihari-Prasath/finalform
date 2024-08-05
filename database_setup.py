import sqlite3

def create_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create willing_users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS willing_users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            qualification TEXT,
            designation TEXT,
            total_experience INTEGER,
            experience_in_nscet INTEGER,
            topics TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Create not_willing_users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS not_willing_users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            qualification TEXT,
            designation TEXT,
            total_experience INTEGER,
            experience_in_nscet INTEGER
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()
