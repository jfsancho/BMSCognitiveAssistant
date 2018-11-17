# coding=utf-8

from sqlalchemy import Column, String, Integer, Date, ForeignKey, Time

from sqlalchemy.orm import relationship, backref

from .base import Base


class Request(Base):
    __tablename__='requests'

    RequestID = Column(Integer, primary_key=True)
    Request = Column(String(255))
    Value = Column(Integer)
    RequestHour = Column(Time)
    RequestDate = Column(Date)
    DeviceID = Column(String(100), ForeignKey('devices.DeviceID'))

    device= relationship("Device", backref="requests")

    def __init__(self, Request, Value, RequestHour, RequestDate, device):
        self.Request=Request
        self.Value=Value
        self.RequestHour=RequestHour
        self.RequestDate=RequestDate
        self.device=device

        
