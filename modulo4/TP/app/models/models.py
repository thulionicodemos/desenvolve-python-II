from app import db, login
from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    remember: Mapped[bool] = mapped_column(default=False)
    last_login: Mapped[datetime] = mapped_column(nullable=True)
    photo: Mapped[str] = mapped_column(nullable=True)
    bio: Mapped[str] = mapped_column(nullable=True)
    posts: Mapped[list['Post']] = relationship(back_populates='author')

    def __repr__(self):
        return f'<User {self.username}>'

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

class Post(db.Model):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(primary_key=True)
    body: Mapped[str] = mapped_column(nullable=False)
    timestamp: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('users.id'), nullable=False)
    author: Mapped[User] = relationship(back_populates='posts')

    def __repr__(self):
        return f'<Post {self.body[:20]}...>'
