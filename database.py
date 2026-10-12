
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime


Base = declarative_base()


class StockRecord(Base):
    __tablename__ = 'stock_history'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime, default=datetime.utcnow)
    ticker = Column(String)
    price = Column(Float)


engine = create_engine('sqlite:///stocks.db', echo=False)
SessionLocal = sessionmaker(bind=engine)


def init_db():
    Base.metadata.create_all(engine)