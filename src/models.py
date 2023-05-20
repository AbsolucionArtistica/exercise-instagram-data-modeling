import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(25), unique=True, nullable=False)
    user_picture_url = Column(String(200))
    first_name = Column(String(25), unique=True, nullable=False)
    last_name = Column(String(25), nullable=False)
    email = Column(String(30), nullable=False)
    password = Column(String(100), nullable=False)
    user_description = Column(String(200))

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    follower_name = Column(String(25), unique=True, nullable=False)
    user = relationship(User)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    post_description = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    post = relationship(Post)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
