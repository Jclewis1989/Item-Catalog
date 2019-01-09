import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }

class ItemCategory(Base):
    __tablename__ = 'item_category'

    id = Column(Integer, primary_key=True)
    description = Column(String(80), nullable=False)
    category = Column(String(80))
    item_id = Column(Integer, ForeignKey('item.id'))
    item = relationship(Item)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'description': self.description,
            'category': self.category
        }

engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)