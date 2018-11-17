# coding=utf-8

from sqlalchemy import Column, String, Integer, Date, ForeignKey

from sqlalchemy.orm import relationship, backref

from .base import Base

class User(Base):
    __tablename__= 'users'

    UserID = Column(String(100), primary_key=True)
    UserName = Column(String(100))
    UserLastName = Column(String(100))
    UserTypeID = Column(Integer,ForeignKey('usertypes.UserTypeID'))
    Password = Column(String(255))

    userType =relationship("Usertype", backref="users")

    def __init__(self, UserID, UserName, UserLastName, Password, userType ):
        self.UserID=UserID
        self.UserName=UserName
        self.UserLastName=UserLastName
        self.userType=userType
        self.Password=Password
