# coding=utf-8

from sqlalchemy import Column, String, Integer

from sqlalchemy.orm import relationship, backref

from .base import Base


class Devicetype(Base):
    __tablename__ = 'devicetypes'

    DeviceType = Column(String(100), primary_key=True)
    Protocol = Column(String(50))

    def __init__(self, DeviceType, Protocol):
        self.DeviceType = DeviceType
        self.Protocol = Protocol
