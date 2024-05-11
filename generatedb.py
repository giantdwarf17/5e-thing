import sqlite3
import json

con = sqlite3.connect("spells.db")
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS spells (name)')

with open('spells-phb.json') as json_file:
   spells = json.load(json_file)
   for spell in spells['spell']:
      for i in spell:
         cur.execute('SELECT * FROM spells')
         columns = list(map(lambda x: x[0], cur.description))
         if not i in columns:
            cur.execute(f'ALTER TABLE spells ADD COLUMN {i}')
         cur.execute(f'INSERT INTO spells ({i}) VALUES (?, ?)', spell[i])

