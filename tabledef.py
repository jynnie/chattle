from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///messages.db', echo=True)
Base = declarative_base()

class Messages(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    message = Column(String)
    #password = Column(String)

    def __init__(self, username):
        self.username = username
        #self.password = password

Base.metadata.create_all(engine)
