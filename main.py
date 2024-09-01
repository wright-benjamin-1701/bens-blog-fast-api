from fastapi import FastAPI
import sqlite3


DB = "quotes.sqlite"

app = FastAPI()

def row_to_json(row):
    return {"_id":row[0],"author":row[1],"book":row[2],"quote":row[3]}

def get_random_row():

    conn = sqlite3.connect(DB)
    curs = conn.cursor()
    row = curs.execute('SELECT _id, author, book, quote FROM Quotes ORDER BY RANDOM() LIMIT 1').fetchone()
    conn.close()

    return row

@app.get("/")
def read_root():
    return {"_id":"0","author":"Kurt Vonnegut","book":"Slaughterhouse-Five","quote":"So it goes."}

@app.get("/random")
def random_quote():
    return row_to_json(get_random_row())
