import sqlite3

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
        c.execute(command)
        
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print ("Tables:")
    
    for t in c.fetchall() :
        print ("\t[%s]"%t[0])
        print ("\tColumns of", t[0])
        c.execute("PRAGMA table_info(%s);"%t[0])
        
        for attr in c.fetchall() :
            print ("\t\t", attr)
            
        print()
        
    conn.commit()
    conn.close()
    
creating()