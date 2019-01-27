from datetime import *
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__="User"
    id=Column(Integer, primary_key = True)
    user_name=Column(String)
    password=Column(String)

    def __repr__(self):
        return("user name: {},password:{}".format(self.user_name,self.password))

class Content(Base):
    __tablename__="Content"
    id=Column(Integer, primary_key = True)
    title=Column(String)
    op=Column(String, nullable=False)
    time_of_upload=Column(DateTime)
    text=Column(String)
    image=Column(String)

    def __repr__(self):
        return "Title: {} \n Original Poster: {} \n Time of Upload: {} \n Text: {} \n Image: {}".format(self.title,self.op,self.time_of_upload,self.text,self.image)

class Content2(Base):
    __tablename__="Content2"
    id=Column(Integer, primary_key = True)
    title=Column(String)
    op=Column(String, nullable=False)
    time_of_upload=Column(DateTime)
    text=Column(String)
    image=Column(String)

    def __repr__(self):
        return "Title: {} \n Original Poster: {} \n Time of Upload: {} \n Text: {} \n Image: {}".format(self.title,self.op,self.time_of_upload,self.text,self.image)



