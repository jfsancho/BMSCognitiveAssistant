# coding=utf-8

from sqlalchemy import Column, String, Integer, ForeignKey

from sqlalchemy.orm import relationship, backref

from .base import Base

class Userrequest(Base):
    __tablename__= 'userrequests'

    UserRequestID = Column(Integer, primary_key=True)
    UserID = Column(String(100), ForeignKey('users.UserID'))
    RequestID = Column(Integer, ForeignKey('requests.RequestID'))

    user = relationship("User", backref="userrequests")
    request = relationship("Request", backref="userrequests")

    def __init__(self, user, request):
        self.user = user
        self.request = request
