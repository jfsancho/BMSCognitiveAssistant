# coding=utf-8

from sqlalchemy import Column, String, Integer, ForeignKey

from sqlalchemy.orm import relationship, backref

from .base import Base

class Device(Base):
    __tablename__= 'devices'

    DeviceID = Column(String(100),primary_key=True)
    SubType=Column(String(100))
    Description = Column(String(100))
    Location = Column(String(100))
    DeviceTypeID = Column(String(100),ForeignKey('devicetypes.DeviceType'))

    deviceType= relationship("Devicetype", backref="devices")

    def __init__(self, DeviceID, SubType, Description, Location, deviceType):
        self.DeviceID = DeviceID
        self.SubType=SubType
        self.Description= Description
        self.Location = Location
        self.deviceType = deviceType
