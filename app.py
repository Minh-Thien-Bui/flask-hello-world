import psycopg2
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


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
    
    response_string = ""
    directory = "models/"
    all_tables = ["account", "body_part", "equipment", "exercise", "favorite"]
    
    for table in all_tables:
        path = directory + table + ".txt"

        sql = open(path, "r")
        command = sql.read()
        sql.close()

        try:
            cur.execute(command)
            conn.commit()
            
        except:
            response_string += "Failed: "
            
        response_string += command 
        response_string += "<br><br>"
        
    conn.close()
    return response_string


@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect("postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a.oregon-postgres.render.com/hulk")
    cur = conn.cursor()
    
    response_string = ""
    directory = "models/insert_"
    all_tables = ["account", "body_part", "equipment", "exercise", "favorite"]
    
    for table in all_tables:
        path = directory + table + ".txt"

        sql = open(path, "r")
        command = sql.read()
        sql.close()

        try:
            cur.execute(command)
            conn.commit()
            
        except:
            response_string += "Failed: "
        
        response_string += command 
        response_string += "<br><br>"
        
    conn.close()
    return response_string


@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a.oregon-postgres.render.com/hulk")
    cur = conn.cursor()
    
    response_string = ""
    all_tables = testing()
    
    for table in all_tables:
        command = "SELECT * FROM " + table
        cur.execute(command)
        records = cur.fetchall()
        
        response_string += table
        response_string += "<table>"

        for player in records:
            response_string += "<tr>"

            for info in player:
                response_string += "<td>{}</td>".format(info)

            response_string += "<tr>"

        response_string += "<table><br>"
    
    conn.close()
    return response_string


@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect("postgres://hulk_user:sJ7uTRAXdhTsJQGOLD9Yq0uhsVBchdAE@dpg-cgrkvt1mbg5e4kh44l70-a.oregon-postgres.render.com/hulk")
    cur = conn.cursor()
    
    response_string = ""
    all_tables = ["favorite", "exercise", "account", "body_part", "equipment"]
    
    for table in all_tables:
        command = "DROP TABLE IF EXISTS " + table + ";"
        
        try:
            cur.execute(command)
            conn.commit()
        
        except:
            response_string += "Failed: "
            
        response_string += command
        response_string += "<br><br>"
        
    conn.close()
    return response_string
