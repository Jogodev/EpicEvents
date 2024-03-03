from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from utils.utils import Base


class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True, unique=True)
    start_date = Column(Date())
    end_date = Column(Date())
    location = Column(String(100))
    Attendees = Column(String(10))
    notes = Column(String())
    contract_id = Column(Integer, ForeignKey('contract.id'))
    contract = relationship('Contract')
    customer_id = Column(Integer, ForeignKey('customer.id'))
    customer = relationship('Customer')
    support_contact = Column(String, ForeignKey('collaborater.name'))
    collaborater = relationship('Collaborater')
    
    def __repr__(self):
        return f'Evennement : {self.name}'
