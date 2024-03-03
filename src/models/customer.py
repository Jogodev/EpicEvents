from utils.utils import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey


class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(50), unique=True)
    email = Column(String(100), unique=True)
    phone = Column(String(100), unique=True)
    company = Column(String(100))
    created_at = Column(Date())
    updated_at = Column(Date())
    collaborater_name = Column(String, ForeignKey('collaborater.name'))
    collaborater = relationship('Collaborater')
    contracts = relationship('Contract', backref='customers')
    events = relationship('Event', backref='customers')

    
    def __repr__(self):
        return f'Clients : {self.name}'
    
