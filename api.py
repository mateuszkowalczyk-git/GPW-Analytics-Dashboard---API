
import yfinance as yf
from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from database import SessionLocal, StockRecord

app = FastAPI(title="Moje API Giełdowe")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class StockRequest(BaseModel):
    ticker: str

@app.get("/")
def read_root():
    return {"message": "Witaj w API Giełdowym! Przejdź do /docs aby zobaczyć dokumentację."}

@app.get("/stocks")
def get_stocks(db: Session = Depends(get_db)):
    return db.query(StockRecord).order_by(StockRecord.date.desc()).limit(20).all()


@app.post("/stocks", status_code=201)
def add_stock(request: StockRequest, db: Session = Depends(get_db)):
    ticker = request.ticker.upper()
    full_ticker = f"{ticker}.WA"
    

    stock = yf.Ticker(full_ticker)
    data = stock.history(period="1d")
    
    if data.empty:

        raise HTTPException(status_code=404, detail=f"Nie znaleziono spółki: {ticker}")
        
    current_price = round(data['Close'].iloc[0], 2)
    

    new_record = StockRecord(
        date=datetime.now(),
        ticker=ticker,
        price=current_price
    )
    db.add(new_record)
    db.commit()
    db.refresh(new_record) 
    
    return new_record