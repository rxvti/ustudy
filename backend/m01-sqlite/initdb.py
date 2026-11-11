import sqlite3 as sqlite


con = sqlite.connect("books.db")

cur = con.cursor()

cur.execute(	
	"""
	CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER,
        genre TEXT
    )
	"""
)

con.commit()
con.close()

print("DB created successfully!")
