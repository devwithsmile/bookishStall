from app import db  # from the app package __init__
from datetime import datetime


# PUBLICATION TABLE
class Publication(db.Model):
    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'The Publisher is {}'.format(self.name)


# BOOKS TABLE
class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100))
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    # ESTABLISH RELATIONSHIP
    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))

    def __init__(self, title, author, avg_rating, book_format, image, num_pages, pub_id):
        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = book_format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    @classmethod
    def create_book(cls, book_title,book_author,book_rating,book_format,book_img,book_pages,book_pub_id):
        book = cls(title = book_title,
                   author= book_author,
                   avg_rating=book_rating,
                   book_format=book_format,
                   image=book_img,
                   num_pages=book_pages,
                   pub_id=book_pub_id 
                   )

        db.session.add(book)
        db.session.commit()

        return book

    def __repr__(self):
        return '{} by {}'.format(self.title, self.author)