# catlog/routes

from flask import render_template, request, flash, redirect, url_for
from app.catlog import main
from app import db
from app.catlog.models import Book, Publication
from flask_login import login_required
from app.catlog.forms import UpdateBookForm,CreateBookForm

@main.route('/book')
@main.route('/')
def display_books():
    books = Book.query.all()
    return render_template('home.html', books=books)


@main.route('/pubisher/<pub_id>')
def display_publisher(pub_id):
    publisher = Publication.query.filter_by(id=pub_id).first()
    publisher_books = Book.query.filter_by(pub_id=pub_id).all()

    return render_template('publisher.html', publisher=publisher, publisher_books=publisher_books)


@main.route('/book/delete/<book_id>', methods=['GET', 'POST'])
@login_required
def delete_book(book_id):
    book = Book.query.get(book_id)

    if request.method == 'POST':
        db.session.delete(book)
        db.session.commit()

        flash("Book is deleted")
        return redirect(url_for('main.display_books'))
    return render_template('delete_book.html', book=book, book_id=book_id)


@main.route('/book/update/<book_id>',methods=['GET','POST'])
@login_required
def update_book(book_id):
    
    book = Book.query.get(book_id)
    form = UpdateBookForm(obj=book)
    if form.validate_on_submit():
        book.title = form.title.data
        book.format = form.format.data
        book.num_pages = form.num_pages.data

        db.session.add(book)
        db.session.commit()

        flash('Book Updated Successfully')
        return redirect(url_for('main.display_books'))
    return render_template('update_book.html',form=form)


@main.route('/book/create/<pub_id>',methods=['GET','POST'])
@login_required
def create_book(pub_id):
    
   
    form = CreateBookForm()
    form.pub_id.data= pub_id #so that it auto fills on the form.
    
    if form.validate_on_submit():
        book = Book.create_book(
            book_title=form.title.data,
            book_author=form.author.data,
            book_rating=form.avg_rating.data,
            book_format=form.book_format.data, #F of Format should be capital , coz format is a keyword
            book_img=form.img_url.data,
            book_pages=form.pages.data,
            book_pub_id=form.pub_id.data
        )

        
        db.session.add(book)
        db.session.commit()
        flash('Book Created Successfully')
        print("pub id is :"+ pub_id)
        
        return redirect(url_for('main.display_publisher',pub_id=pub_id))
    return render_template('create_book.html',pub_id=pub_id,form=form)


    
