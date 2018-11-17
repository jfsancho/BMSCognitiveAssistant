
from .base import Session, engine, Base

import sys
import traceback
import datetime

from sqlalchemy import and_

from .device import Device
from .devicetype import Devicetype
from .permission import Permission
from .request import Request
from .user import User
from .userrequest import Userrequest
from .usertype import Usertype

class DBController:

    def __init__(self):
        Base.metadata.create_all(engine)

    def createDeviceType(self, DeviceID, protocol):
        newDeviceType = Devicetype(DeviceID, protocol)
        session= Session()
        try:
            session.add(newDeviceType)
            session.commit()
            session.close()
        except Exception:
            print(traceback.format_exc())
        
        return newDeviceType

    def createDevice(self, DeviceID, SubType, Description, Location, device_type):
        newDevice = Device(DeviceID, SubType, Description, Location, device_type)
        session= Session()
        try:
            session.add(newDevice)
            session.commit()
            session.close()
        except Exception:
            print(traceback.format_exc())

        return newDevice

    def createPermission(self,PermissionType):
        newPermission= Permission(PermissionType)
        session= Session()
        try:
            session.add(newPermission)
            session.commit()
            session.close()
        except Exception:
            print(traceback.format_exc())

        return newPermission

    def createUserType(self, user_type, permission):
        newUserType= Usertype( user_type ,permission)
        session= Session()
        try:
            session.add(newUserType)
            session.commit()
            session.close()
        except Exception:
            print(traceback.format_exc())

        return newUserType

    def createUser(self, UserID, UserName, UserLastName, Password, user_type):
        newUser= User(UserID, UserName, UserLastName, Password, user_type)
        session= Session()
        try:
            session.add(newUser)
            session.commit()
            session.close()
        except Exception:
            print(traceback.format_exc())

        return newUser

    def createRequest(self, Request, Value, device, user):
        t= datetime.datetime.now()
        d =datetime.date(t.year, t.month, t.day)
        t= datetime.time(t.hour,t.minute,t.second)
        newRequest = Request(Request, Value, d, t, device)
        newUserRequest = Userrequest(user, newRequest)
        session= Session()
        try:
            session.add(newRequest)
            session.add(newUserRequest)
            session.commit()
            session.close()
        except Exception:
            print(traceback.format_exc())

        return newUserRequest

    def getDevice(self, device_type,location):
        session=Session()
        devices= session.query(Device)\
        .join(Devicetype)\
        .filter( and_(Device.DeviceTypeID == device_type, Device.Location.ilike('%'+location+'%') ) )\
        .all()
        session.close()

        return devices

    def getPermission(self, PermissionID):
        session=Session()
        permission= session.query(Permission)\
        .filter(Permission.PermissionID==PermissionID).first()
        session.close()
        
        return permission

    def getUser(self,userID):
        session=Session()
        user= session.query(User)\
        .filter(User.UserID==userID).first()
        session.close()

        return user