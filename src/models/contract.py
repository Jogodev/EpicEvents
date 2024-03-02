from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from utils.utils import Base

class Contract(Base):
    __tablename__ = 'contract'
    
    id = Column(Integer, primary_key=True, unique=True)
    contract_price = Column(String(10))
    left_to_pay = Column(String(10))
    created_at = Column(Date())
    status = Column(Boolean(), default=False)
    events = relationship('Event', backref='contracts', uselist=False)
    collaborater_name = Column(String, ForeignKey('collaborator.name'))
    collaborater = relationship('Collaborater')
    customer_name = Column(Integer, ForeignKey('customer.name'))
    customer = relationship('Customer')
    
    
    def __repr__(self):
        return f'Contrat : {self.name}'