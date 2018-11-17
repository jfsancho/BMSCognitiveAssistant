# coding=utf-8

from sqlalchemy import Column, String, Integer, Date

from sqlalchemy.orm import relationship

from .base import Base

class Permission(Base):
    __tablename__= 'permissions'

    PermissionID = Column(Integer, primary_key = True)
    PermissionType = Column(String(255))
    #UserType= =relationship("Usertype", back_populates="")

    def __init__(self, PermissionType):
        self.PermissionType = PermissionType
