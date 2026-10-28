from sqlalchemy import Column, Integer, String, Float
from database import BASE

class Expense(BASE):
    __tablename__="expenses"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    amount = Column(Float,nullable=False)
    category = Column(String, nullable=False)
    
class Category(BASE):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)