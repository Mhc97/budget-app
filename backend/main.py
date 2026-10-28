from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import model
import schema
from database import SessionLocal, engine, get_db
from pydantic import BaseModel, Field

# Créer les tables dans la DB
model.BASE.metadata.create_all(bind=engine)

app = FastAPI()

# autorise react à appeler l'api
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===== ENDPOINTS =====

@app.get("/")
def read_root():
    return {"message": "Budget API fonctionne 🎉"}

# GET all expenses

@app.get("/expenses", response_model=list[schema.Expense])
def get_expenses(db: Session = Depends(get_db)):
    return db.query(model.Expense).all()

# GET one expense

@app.get("/expenses/{expense_id}", response_model=schema.Expense)
def get_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(model.Expense).filter(model.Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense

# POST create expense
@app.post("/expenses", response_model=schema.Expense)
def create_expense(expense: schema.ExpenseCreate, db: Session = Depends(get_db)):
    db_expense = model.Expense(**expense.dict())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

# PUT updat expense
@app.put("/expenses/{expense_id}", response_model=schema.Expense)
def update_expense(
    expense_id: int,
    expense: schema.ExpenseCreate,
    db: Session = Depends(get_db)
):
    db_expense = db.query(model.Expense).filter(model.Expense.id == expense_id).first()
    if not db_expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    for key, value in expense.dict().items():
        setattr(db_expense, key, value)
        
    db.commit()
    db.refresh(db_expense)
    return db_expense


# DELETE expense
@app.delete("/expense/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    db_expense = db.query(model.Expense).filter(model.Expense.id == expense_id).first()
    if not db_expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    db.delete(db_expense)
    db.commit()
    return {"message":"Expense deleted"}

class ExpenseBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    amount: float = Field(..., gt=0)
    category: str = Field(..., min_length=1, max_length=50)
    
