#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import String
from models.base_model import BaseModel
from sqlalchemy.sql.schema import Column, ForeignKey

class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place")
