import sqlite3
import json

con = sqlite3.connect("spells.db")
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS spells (name)')

with open('spells-phb.json') as json_file:
    spells = json.load(json_file)
    for spell in spells['spell']:
       for i in spell:
          print(i)
          try:
             cur.execute(f"""
                      ALTER TABLE spells
                      ADD {i}""")
          except sqlite3.OperationalError:
             pass
          
          cur.execute(f"""
                      INSERT INTO spells ("{i}")
                      VALUES ("{spell[i]}");
                      """)