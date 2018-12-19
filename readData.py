from main import User, SetterGetter, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///UserDatabase.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

userName = input("Enter the user name to be searched")
password = input("enter the password for the user")
session.query(User).all()
user = session.query(User).filter(User.userName == userName).filter(User.password == password).first()
settergetterObject = SetterGetter(0, userName, password)
print(settergetterObject.userName)
print(settergetterObject.password)
