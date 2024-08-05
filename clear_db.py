import sqlite3

def clear_database():
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # SQL commands to delete all records from the tables
    cursor.execute('DELETE FROM willing_users')
    cursor.execute('DELETE FROM not_willing_users')

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

    print("All data has been removed from the database.")

if __name__ == '__main__':
    clear_database()
