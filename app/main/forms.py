from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,TextAreaField,PasswordField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User,Blog,Comment
from wtforms import ValidationError


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


class BlogForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    blog = TextAreaField('Your Blog', validators=[Required()])
    submit = SubmitField('post')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[Required()])
    submit = SubmitField('Comment')
