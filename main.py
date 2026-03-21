from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from schemas import ExpenseCreate, ExpenseResponse
from database import get_db, Base, engine
from typing import List
from crud import create_expense_crud, get_expenses_crud, get_expenses_by_id_crud, delete_expense_crud, update_expense_crud

## API Endpoint'lerini çalıştırıyoruz.
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Expense Tracker API is Running"}

@app.post("/expenses")
def create_expense(expense: ExpenseCreate, db: Session = Depends(get_db)): #Yeni expense yaratıp db 'ye ekliyor.
    return create_expense_crud(expense, db)

@app.get("/expenses", response_model= List[ExpenseResponse]) #Request'in yapılması durumunda db'den verinin çekilip client'e geri döndürülmesi.
def get_expenses(db: Session = Depends(get_db)):
    return get_expenses_crud(db)

@app.get("/expenses/{expense_id}", response_model= ExpenseResponse)  #Request'in id'ye göre yapılması durumunda db'den verinin çekilip client'e geri döndürülmesi.
def get_expenses_by_id(expense_id: int, db: Session = Depends(get_db)):
    return get_expenses_by_id_crud(expense_id, db)

@app.delete("/expenses/{expense_id}", response_model = ExpenseResponse)
def delete_expense(expense_id: int, db: Session= Depends(get_db)):
    return delete_expense_crud(expense_id, db)

@app.put("/expenses/{expense_id}", response_model = ExpenseResponse)
def update_expense(expense_id: int, expense: ExpenseCreate , db: Session = Depends(get_db)):
    return update_expense_crud(expense_id, expense, db)