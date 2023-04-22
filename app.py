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
    
    cur = conn.cursor()
    cur.execute("""SELECT relname FROM pg_class WHERE relkind='r'
    AND relname !~ '^(pg_|sql_)';""") # "rel" is short for relation.

    tables = [i[0] for i in cur.fetchall()] # A list() of tables.
    
    conn.close()
    return tables

    
@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a.oregon-postgres.render.com/hulk")
    cur = conn.cursor()
    
    all_tables = ["body_part", "exercise", "equipment", "account", "favorite"]
    directory = "models/"
    
    for table in all_tables:
        path = directory + table + ".txt"

        sql = open(path, "r")
        command = sql.read()
        sql.close()

        cur.execute(command)
        
    conn.commit()
    conn.close()
    
    return "All Tables Successfully Created"

@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect("postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a.oregon-postgres.render.com/hulk")
    cur = conn.cursor()
    
    cur.execute('''
        INSERT INTO account Values
        (23, 'LeBron', 'KingJames@nba.com'),
        (24, 'Kobe', 'BeanBryant@nba.com');
    ''')
    
    conn.commit()
    conn.close()
    return "Account Table Successfully Populated"

@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a.oregon-postgres.render.com/hulk")
    
    cur = conn.cursor()
    all_tables = testing()
    response_string = ""
    
    for table in all_tables:
        command = "SELECT * FROM " + table
        cur.execute(command)
        records = cur.fetchall()
        
        response_string += table
        response_string += "\n<table>"

        for player in records:
            response_string += "<tr>"

            for info in player:
                response_string += "<td>{}</td>".format(info)

            response_string += "<tr>"

        response_string += "<table>\n"
    
    conn.close()
    return response_string

@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect("postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a.oregon-postgres.render.com/hulk")
    
    cur = conn.cursor()
    all_tables = testing()
    
    for table in all_tables:
        command = "DELETE FROM " + table
        cur.execute(command)
        
    conn.commit()
    conn.close()
    return "All Tables Successfully Cleared"
