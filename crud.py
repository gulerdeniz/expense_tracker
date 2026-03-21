from sqlalchemy.orm import Session
from schemas import ExpenseCreate
from models import Expense
from fastapi import HTTPException
from typing import List

def create_expense_crud(expense: ExpenseCreate, db: Session) -> Expense:
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

def get_expenses_crud(db: Session) -> List[Expense]:
    expenses = db.query(Expense).all()
    return expenses

def get_expenses_by_id_crud(expense_id: int, db: Session) -> Expense:
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if expense == None:
        raise HTTPException(status_code = 404, detail = "Expense not found")
    return expense

def delete_expense_crud(expense_id: int, db: Session) -> dict[str, str]:
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if expense == None:
        raise HTTPException(status_code = 404, detail = "Expense not found")
    db.delete(expense)
    db.commit()
    return {"message":"Expense deleted"}

def update_expense_crud(expense_id: int, expense: ExpenseCreate , db: Session) -> Expense:
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