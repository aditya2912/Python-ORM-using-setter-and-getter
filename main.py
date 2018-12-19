import os
import sys
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    userName = Column(String, nullable=False)
    password = Column(String, nullable=False)

engine = create_engine('sqlite:///UserDatabase.db')
Base.metadata.create_all(engine)

class SetterGetter:
    id = 0
    userName = ""
    password = ""

    def setter(self, id, userName, password):
        self.id = id
        self.userName = userName
        self.password = password

    def __init__(self, id, userName, password):
        self.id = id
        self.userName = userName
        self.password = password
