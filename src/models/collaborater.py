from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.utils.utils import Base

class Collaborater(Base):
    __tablename__ = 'collaborater'
    
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    password = Column(String)
    role = Column(String(50))
    customers = relationship('Customer', backref='customers_collaboraters')
    contracts = relationship('Contract', backref='contracts_collaboraters')
    events = relationship('Event', backref='events_collaboraters')
    
    def __repr__(self):
        return f'Collaborateur : {self.name}'