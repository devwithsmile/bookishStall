from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,FloatField,IntegerField
from wtforms.validators import DataRequired

class UpdateBookForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    format = StringField('Format', validators=[DataRequired()])
    num_pages= StringField('Pages',validators=[DataRequired()])
    submit=SubmitField("Update")


class CreateBookForm(FlaskForm):
    title=StringField('Title of the Book ',validators=[DataRequired()])
    author=StringField("author of the Book",validators=[DataRequired()])
    avg_rating=FloatField("rating of the Book",validators=[DataRequired()])
    book_format=StringField("format of the Book",validators=[DataRequired()])
    img_url=StringField("image url of the Book",validators=[DataRequired()])
    pages=IntegerField("no. of pages ",validators=[DataRequired()])
    pub_id = IntegerField("Publisher ID: ", validators=[DataRequired()])
    submit = SubmitField("Create Book")
  


