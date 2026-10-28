from pydantic import BaseModel

class ExpenseBase(BaseModel):
    title: str
    amount: float
    category: str
    
class ExpenseCreate(ExpenseBase):
    pass

class Expense(ExpenseBase):
    id: int
    
    class Config:
        from_attributes = True 
        # Pydabtic v2 -> permet de convertir des objet SQLAlchemy en Pydantic
        # orm_mode = True # Pydantic v1 
    