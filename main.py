from fastapi import FastAPI
import sqlite3

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# You can add additional URLs to this list, for example, the frontend's production domain, or other frontends.
allowed_origins = [
    "http://localhost:3000",
    "https://benwright.blog",
    "https://bens-blog-react-tfeo4yp7iq-uc.a.run.app"
]




DB = "quotes.sqlite"

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["X-Requested-With", "Content-Type"],
)

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
