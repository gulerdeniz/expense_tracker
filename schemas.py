from pydantic import BaseModel
from datetime import date

## API'dan gelen verinin validasyon'unu (doğrulamasını) yapıyoruz.
class ExpenseCreate(BaseModel):
    amount: float
    category: str
    description: str | None = None
    date: date

class ExpenseResponse(BaseModel):
    id: int
    amount: float
    category: str
    description: str | None = None
    date: date

    class Config:
        from_attributes = True