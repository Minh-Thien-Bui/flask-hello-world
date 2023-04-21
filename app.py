import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hulk Smash!'


@app.route('/db_test')
def testing():
    #conn = psycopg2.connect("postgres://bui_minh_db_user:L2TSBM9xSicOTaRmsIMVwBjPPh4ifjQC@dpg-cglto707oslael5ffs80-a/bui_minh_db")
    
    #conn = psycopg2.connect("postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a/hulk")
    
    conn = psycopg2.connect("postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a.oregon-postgres.render.com/hulk")
    
    conn.close()
    
    return "Connected to Hulk"
  
    
@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a.oregon-postgres.render.com/hulk")
    cur = conn.cursor()
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS account (
        account_id INT PRIMARY KEY,
        username VARCHAR(15) UNIQUE,
        email VARCHAR(320) UNIQUE);
    ''')
    
    conn.commit()
    conn.close()
    return "Account Table Successfully Created"

@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect("postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a.oregon-postgres.render.com/hulk")
    cur = conn.cursor()
    
    cur.execute('''
        INSERT INTO account (account_id, username, email)
        Values
        (23, 'LeBron', 'KingJames@nba.com');
    ''')
    
    conn.commit()
    conn.close()
    return "Account Table Successfully Populated"

@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a.oregon-postgres.render.com/hulk")
    
    cur = conn.cursor()
    data = cur.execute("SELECT * FROM account")

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
    conn = psycopg2.connect("postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a.oregon-postgres.render.com/hulk")
    cur = conn.cursor()
    cur.execute('''
        DELETE FROM account;
    ''')
    conn.commit()
    conn.close()
    return "Account Table Successfully Cleared"
