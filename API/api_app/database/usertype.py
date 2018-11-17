# coding=utf-8
from sqlalchemy import Column, String, Integer, ForeignKey

from sqlalchemy.orm import relationship, backref

from .base import Base


class Usertype(Base):
    __tablename__='usertypes'

    UserTypeID = Column(Integer,primary_key=True)
    UserType = Column(String(100))
    PermissionID =Column(Integer, ForeignKey('permissions.PermissionID'))

    permission = relationship("Permission", backref = "usertypes")

    def __init__(self, UserType, permission):
        self.UserType=UserType
        self.permission=permission
