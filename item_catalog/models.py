import os
import sys
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()

"""
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'email': self.email
        }
"""

class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    created_date = Column(DateTime, default=datetime.utcnow)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'created_date': self.created_date,
        }

class ItemCategory(Base):
    __tablename__ = 'item_category'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    price = Column(String(80), nullable=False)
    description = Column(String(80), nullable=False)
    category = Column(String(80), nullable=False)
    stock = Column(String(80), nullable=False)
    item_id = Column(Integer, ForeignKey('item.id'))
    item = relationship(Item, backref=backref("item", cascade="all,delete"))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'description': self.description,
            'category': self.category,
            'name': self.name,
            'price': self.price,
            'stock': self.stock,
        }

engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)