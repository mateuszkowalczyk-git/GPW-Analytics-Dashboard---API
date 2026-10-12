
import yfinance as yf
from datetime import datetime


from database import init_db, SessionLocal, StockRecord

def get_stock_price(ticker: str):
    full_ticker = f"{ticker}.WA"
    stock = yf.Ticker(full_ticker)
    data = stock.history(period="1d")
    
    if data.empty:
        print(f"Nie znaleziono danych dla {ticker}")
        return None
        
    current_price = data['Close'].iloc[0]
    return round(current_price, 2)

if __name__ == "__main__":

    init_db()
    

    session = SessionLocal()
    
    moje_spolki = ["XTB", "PKO", "CDR", "PKN", "KGH"]
    print("Rozpoczynam pobieranie danych...\n")

    for ticker in moje_spolki:
        price = get_stock_price(ticker)
        
        if price:
            new_record = StockRecord(
                date=datetime.now(),
                ticker=ticker,
                price=price
            )
            session.add(new_record)
            print(f"Pobrano i dodano do sesji: {ticker} -> {price} PLN")
            

    session.commit()
    print("\n✅ Zapisano pomyślnie w bazie!")
    

    print("\nOstatnie wpisy w bazie:")
    ostatnie = session.query(StockRecord).order_by(StockRecord.date.desc()).limit(5).all()
    
    for rekord in ostatnie:
        print(f"[{rekord.date.strftime('%Y-%m-%d %H:%M:%S')}] {rekord.ticker}: {rekord.price} PLN")
        

    session.close()