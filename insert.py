from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main import Base, User, SetterGetter

engine = create_engine('sqlite:///UserDatabase.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()
userName = input("Enter the userName")
password = input("Enter the password for the user")
userData = User(userName=userName, password=password)
session.add(userData)
try:
    session.commit()
    print("User data successfully submitted.")
    session.close()
except IOError:
    print("Error in inserting data")
