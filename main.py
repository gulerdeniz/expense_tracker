from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import ExpenseCreate, ExpenseResponse
from database import get_db, Base, engine
from models import Expense
from typing import List

## API Endpoint'lerini çalıştırıyoruz.
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Expense Tracker API is Running"}

@app.post("/expenses")
def create_expense(expense: ExpenseCreate, db: Session = Depends(get_db)): #Yeni expense yaratıp db 'ye ekliyor.
    new_expense = Expense(
        amount = expense.amount,
        category = expense.category,
        description = expense.description,
        date = expense.date
      )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

@app.get("/expenses", response_model= List[ExpenseResponse]) #Request'in yapılması durumunda db'den verinin çekilip client'e geri döndürülmesi.
def get_expenses(db: Session = Depends(get_db)):
    expenses = db.query(Expense).all()
    return expenses

@app.get("/expenses/{expense_id}", response_model= ExpenseResponse)  #Request'in id'ye göre yapılması durumunda db'den verinin çekilip client'e geri döndürülmesi.
def get_expenses_by_id(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if expense == None:
        raise HTTPException(status_code = 404, detail = "Expense not found")
    return expense

@app.get("/expenses/{expense_id}", response_model = ExpenseResponse)
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if expense == None:
        raise HTTPException(status_code = 404, detail = "Expense not found")
    db.delete(expense)
    db.commit()
    return {"message":"Expense deleted"}

@app.put("/expenses/{expense_id}", response_model = ExpenseResponse)
def update_expense(expense_id: int, expense: ExpenseCreate , db: Session = Depends(get_db)):
    current_expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if current_expense == None:
        raise HTTPException(status_code = 404, detail = "Expense not found")
    
    current_expense.amount = expense.amount
    current_expense.category = expense.category
    current_expense.description = expense.description
    current_expense.date = expense.date

    db.commit()
    db.refresh(current_expense)

    return current_expense