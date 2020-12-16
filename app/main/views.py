from flask import render_template,request,redirect,url_for,abort,flash
from flask_login import login_required,current_user
from ..models import Blog,Comment,User,Subscriber
from .forms import BlogForm,CommentForm,UpdateProfile
from .. import db,photos
from . import main
from ..email import mail_message


@main.route('/')
def index():
    """
    views root page function that returns the index page
    """
    return render_template('index.html')


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(author = uname).first()
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(author = uname).first()
    if user is None:
        abort(404)
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile',uname=user.author))
    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(author = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/comment/<blog_id>', methods = ['Post','GET'])
@login_required
def comment(blog_id):
    blog = Blog.query.get(blog_id)
    comment =request.form.get('newcomment')
    new_comment = Comment(comment = comment, user_id = current_user._get_current_object().id, blog_id=blog_id)
    new_comment.save()
    return redirect(url_for('main.blog',id = blog.id))


@main.route('/subscribe',methods = ['POST','GET'])
@login_required
def subscribe():
    email = request.form.get('subscriber')
    new_subscriber = Subscriber(email = email)
    new_subscriber.save_subscriber()
    mail_message("Subscribed to Blog App","email/welcome_subscriber",new_subscriber.email,new_subscriber=new_subscriber)
    flash('Sucessfuly subscribed')
    return redirect(url_for('main.index'))



main.route("/blog/new",methods= ['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        flash('Your blog has been created', 'success')
        return redirect(url_for('main.index'))  

        return render_template('create_blog.html', title='New Blog', form = form)


@main.route('/blog/<blog_id>/update', methods = ['GET','POST'])
@login_required
def update_blog(blog_id):
    blog = Blog.query.get(blog_id)
    if blog.user != current_user:
        abort(403)
    form = CreateBlog()
    if form.validate_on_submit():
        form.title= form.title.data
        form.content= form.content.data
        db.session.commit()
        flash("Your post has benn updated!")
        return redirect(url_for('blog', blog_id=blog_id)) 
    elif request.method == 'GET':
        form.title.data = blog.title
        form.content.data = blog.content
    return render_template('create_blog.html', form = form)