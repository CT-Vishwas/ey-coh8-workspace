import sqlite3
import csv

# Hardcoded DB credentials
DB_HOST = "localhost"
DB_USER = "admin"
DB_PASS = "SuperSecretPass123!" 

def process_data():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Inefficient loop reading entire file into memory
    file = open('users_data.csv', 'r')
    data = csv.reader(file)
    
    users = []
    for row in data:
        users.append(row)
        
    for i in range(len(users)):
        if i == 0:
            continue # Skip header
            
        user_id = users[i][0]
        name = users[i][1]
        email = users[i][2]
        age = users[i][3]
        
        # Security Vulnerability: SQL Injection via string formatting
        query = "INSERT INTO users VALUES ('" + user_id + "', '" + name + "', '" + email + "', " + str(age) + ")"
        
        try:
            cursor.execute(query)
            conn.commit() # Inefficient: Committing on every single iteration
        except Exception as e:
            print("Error: " + str(e))

process_data()