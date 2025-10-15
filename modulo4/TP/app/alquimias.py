from app import db
from app.models.models import User, Post
from datetime import datetime

def validate_user_password(username, password):
    user = db.session.query(User).filter_by(username=username).first()
    if user and user.password == password:
        return user
    return None

def user_exists(username):
    user = db.session.query(User).filter_by(username=username).first()
    return user

def create_user(username, password, remember=False, last_login=None, photo=None, bio=None):
    new_user = User(
        username=username,
        password=password,
        remember=remember,
        last_login=last_login or datetime.utcnow(),
        photo=photo,
        bio=bio
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user

def create_post(body, user):
    post = Post(body=body, author=user, timestamp=datetime.utcnow())
    db.session.add(post)
    db.session.commit()
    return post

def get_timeline():
    return db.session.query(Post).order_by(Post.timestamp.desc()).limit(5).all()