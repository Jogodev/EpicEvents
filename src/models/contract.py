from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from utils.utils import Base
from models import collaborater
from models import event

class Contract(Base):
    __tablename__ = 'contracts'
    
    id = Column(Integer, primary_key=True, unique=True)
    contract_price = Column(String(10))
    left_to_pay = Column(String(10))
    created_at = Column(Date())
    status = Column(Boolean(), default=False)
    
    event_id = Column(Integer, ForeignKey('event.id'))
    collaborater_id = Column(Integer, ForeignKey('collaborator.id'))
    customer_id = Column(Integer, ForeignKey('customer.id'))
    event = relationship('Event', backref='contract', uselist=False)
    
    def __repr__(self):
        return f'Contrat : {self.name}'