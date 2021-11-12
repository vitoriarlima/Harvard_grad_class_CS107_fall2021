import sqlite3

#create a database
db = sqlite3.connect("candidates")

cursor = db.cursor()

cursor.execute("""DROP TABLE IF EXISTS candidates""")

cursor.execute("""CREATE TABLE candidates (
 id INTEGER PRIMARY KEY NOT NULL,
 first_name TEXT,
 last_name TEXT,
 middle_initial TEXT,
 party TEXT NOT NULL)""")
 
with open('candidates.txt') as f:
    next(f)
    for line in f:
        uid, first_name, last_name, middle_initial, party = line.strip().split("|") #strip means that u take away the space at the end
        cursor.execute("""INSERT INTO candidates
        (id, first_name, last_name, middle_initial, party)
        VALUES ( ?, ?, ?, ?, ?)""", (int(uid), first_name, last_name, middle_initial, party))
        

db.commit()
db.close()

