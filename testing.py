import sqlite3

def print_table(cursor, table):
    data = cursor.execute("SELECT * FROM " + table)

    for row in data:
        print(row)

def creating():
    conn = sqlite3.connect("test_tables")
    c = conn.cursor()
    
    directory = "models/"
    
    table_names = [
        "account",
        "body_part",
        "equipment",
        "exercise",
        "favorite"
    ]
    
    for table in table_names:
        path = directory + table + ".txt"
        
        sql = open(path, "r")
        command = sql.read()
        sql.close()
        
        print(command, "\n")
        c.execute(command)
        
    conn.commit()
    conn.close()
    
creating()