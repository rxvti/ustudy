import sqlite3 as sqlite

books = [
	("1984", "George Orwell", 1949, "Dystopian"),
	('Science and Human Behavior', 'B.F. Skinner', 1953, 'Psychology'),
	('The Theory of the Leisure Class', 'Thorstein Veblen', 1899, 'Economics'),
	('The Demon-Haunted World: Science as a Candle in the Dark', 
		'Carl Sagan', 1995, 'Science'),
	('Looking Backward: 2000–1887', 'Edward Bellamy', 1888, 'Science Fiction'),
]

con = sqlite.connect("books.db")
cur = con.cursor()

cur.executemany("INSERT INTO books (title, author, year, genre)\
				 VALUES (?, ?, ?, ?)",
			 	books
			 	)
con.commit()

cur.execute("SELECT * FROM books")
books = cur.fetchall()

for book in books:
	print(book)
con.close()
