from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship


from app.models.products import Product
from app.models import *

class Category(Base):
    __tablename__ = 'category'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    slug = Column(String,unique=True,index=True)
    is_active = Column(Boolean, default=True)
    parent_id = Column(Integer, ForeignKey('category.id'), nullable=True)

    products = relationship('Product', back_populates='category')

from sqlalchemy.schema import CreateTable
print(CreateTable(Category.__table__))

from sqlalchemy.schema import CreateTable
print(CreateTable(Product.__table__))