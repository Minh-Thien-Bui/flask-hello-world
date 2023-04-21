import psycopg2
from flask import Flask
app = Flask(__name__)

table_names = [
    "account",
    "body_part",
    "equipment",
    "exercise",
    "favorite"
]


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
    conn = psycopg2.connect("postgres://bui_minh_db_user:L2TSBM9xSicOTaRmsIMVwBjPPh4ifjQC@dpg-cglto707oslael5ffs80-a/bui_minh_db")
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
    conn = psycopg2.connect("postgres://bui_minh_db_user:L2TSBM9xSicOTaRmsIMVwBjPPh4ifjQC@dpg-cglto707oslael5ffs80-a/bui_minh_db")
    cur = conn.cursor()
    
    cur.execute('''
        INSERT INTO account (?, ?, ?)
        Values
        (0, "user1", "user1@example.com"),
        (1, "user2", "user2@example.com"),
        (2, "user3", "user3@example.com");
    ''')
    
    conn.commit()
    conn.close()
    return "Account Table Successfully Populated"

@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgres://bui_minh_db_user:L2TSBM9xSicOTaRmsIMVwBjPPh4ifjQC@dpg-cglto707oslael5ffs80-a/bui_minh_db")
    cur = conn.cursor()
    
    data = cur.execute("SELECT * FROM account")

    for row in data:
        print(row)

@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect("postgres://bui_minh_db_user:L2TSBM9xSicOTaRmsIMVwBjPPh4ifjQC@dpg-cglto707oslael5ffs80-a/bui_minh_db")
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE account;
    ''')
    conn.commit()
    conn.close()
    return "Account Table Successfully Dropped"
