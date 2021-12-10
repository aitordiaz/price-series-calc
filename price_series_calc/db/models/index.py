from sqlalchemy import Column, Integer, Float

from price_series_calc.db.config import Base


class Index(Base):
    __tablename__ = 'indices'

    id = Column(Integer, primary_key=True)
    weight = Column(Integer, nullable=False)
    prices = Column(Float, nullable=False)
