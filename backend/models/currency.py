from sqlalchemy import Column, Integer, String, Float
from databese import Base

class Currency(Base):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    rate = Column(Float)
