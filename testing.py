import sqlite3

table_names = [
    "account",
    "body_part",
    "equipment",
    "exercise",
    "favorite"
]


insertions = {
    "body_part": [
        (0, "Arms", "Bicep Curl"),
        (1, "Back", "Rows"),
        (2, "Legs", "Squats"),
        (3, "Abs", "Sit-Ups"),
        (4, "Cardio", "Running")
    ],
    
    "equipment": [
        (0, "None"),
        (1, "Dumbells"),
        (2, "Single Dumbell"),
        (3, "Body Weight")
    ],
    
    "exercise": [
        (0, "Bicep Curl", "Curls dumbbells from a standing position", 
         "Arms", "Dumbells"),
        
        (1, "Rows", "Pulls dumbbells towards the chest while bending over", 
         "Back", "Dumbells"),
        
        (2, "Squats", "Lowers body by bending at the hips and knees", 
         "Legs", "Body Weight"),
        
        (3, "Sit-Ups", 
         "Lifts upper body towards knees while lying on the ground", 
         "Abs", "Body Weight"),
        
        (4, "Running", "Fast-paced movement using legs and feet", 
         "Cardio", "None")
    ],
    
    "account": [
        (0, "user1", "user1@example.com"),
        (1, "user2", "user2@example.com"),
        (2, "user3", "user3@example.com")
    ],
    
    "favorite": [
        (0, "user1", "Bicep Curl"),
        (1, "user2", "Rows"),
        (2, "user3", "Squats")
    ]
}


def creating():
    conn = sqlite3.connect("test_tables")
    c = conn.cursor()
    
    directory = "models/"
    
    for table in table_names:
        path = directory + table + ".txt"
        
        sql = open(path, "r")
        command = sql.read()
        sql.close()
        
        print(command, "\n")
        c.execute(command)
        
    conn.commit()
    conn.close()

    
def insert(value, table, c):
    command = "INSERT INTO " + table + " VALUES ("
    
    col_count = c.execute(
        "SELECT count() FROM PRAGMA_TABLE_INFO('" + table + "');"
    )
    
    col_count = col_count.fetchall()
    col_count = col_count[0][0]
    
    for i in range(col_count - 1):
        command += "?, "
    
    command += "?);"
    c.execute(command, value)
    
    
def inserting():
    conn = sqlite3.connect("test_tables")
    c = conn.cursor()
    
    for table, value_list in insertions.items():
        for value in value_list:
            insert(value, table, c)
            
    conn.commit()
    conn.close()
    
    
def selecting():
    conn = sqlite3.connect("test_tables")
    c = conn.cursor()
    
    for table in table_names:
        data = c.execute("SELECT * FROM " + table)

        for row in data:
            print(row)
            
        print()

    conn.close()

creating()
inserting()
selecting()
