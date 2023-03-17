from app import app, db
from sqlalchemy.sql import func
import json


class Book(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), unique=True, nullable=False)
	author = db.Column(db.String(100), nullable=False)
	genre = db.Column(db.String(20), nullable=False)
	cover = db.Column(db.String(50), nullable=False, default='default.jpg')
	description = db.Column(db.Text)

	def __repr__(self):
            return f'<Book {self.title}>'	
        
with open('books.json', encoding="utf8") as f:
	books_json = json.load(f)
	for book in books_json:
		book = Book(title=book['title'], 
	      author=book['author'],
	      genre=book['genre'],  
	      description=book['description']
)
		db.session.add(book)
		db.session.commit()		
