#!/usr/bin/python3
"""
Module that connects to the database
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.delarative import declarative_base

Base = declarative_base()

class State(Base):
    """Defines the state classs"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
