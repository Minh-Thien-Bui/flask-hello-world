import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/db_test')
def testing():
    #conn = psycopg2.connect("postgres://bui_minh_db_user:L2TSBM9xSicOTaRmsIMVwBjPPh4ifjQC@dpg-cglto707oslael5ffs80-a/bui_minh_db")
    
    #conn = psycopg2.connect("postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a/hulk")
    
    conn = psycopg2.connect("postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a.oregon-postgres.render.com/hulk")
    c = conn.cursor()
    
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print ("Tables:")
    
    for t in c.fetchall() :
        print ("\t[%s]"%t[0])
        print ("\tColumns of", t[0])
        c.execute("PRAGMA table_info(%s);"%t[0])
        
        for attr in c.fetchall() :
            print ("\t\t", attr)
            
        print()
    
    conn.close()
  
    
@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a.oregon-postgres.render.com/hulk")
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

@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect("postgres://bui_minh_db_user:L2TSBM9xSicOTaRmsIMVwBjPPh4ifjQC@dpg-cglto707oslael5ffs80-a/bui_minh_db")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"

@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgres://bui_minh_db_user:L2TSBM9xSicOTaRmsIMVwBjPPh4ifjQC@dpg-cglto707oslael5ffs80-a/bui_minh_db")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
    ''')
    records = cur.fetchall()
    conn.close()
    
    response_string = ""
    response_string += "<table>"
    
    for player in records:
        response_string += "<tr>"
        
        for info in player:
            response_string += "<td>{}</td>".format(info)
            
        response_string += "<tr>"
        
    response_string += "<table>"
    
    return response_string

@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect("postgres://bui_minh_db_user:L2TSBM9xSicOTaRmsIMVwBjPPh4ifjQC@dpg-cglto707oslael5ffs80-a/bui_minh_db")
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"
