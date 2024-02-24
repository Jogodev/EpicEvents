from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from utils.utils import Base

class Collaborater(Base):
    __tablename__ = 'collaborator'
    
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(100))
    
    contract_id = Column(Integer, ForeignKey('contract.id'), nullable=True)
    customers = relationship('Customer', backref='collaborater')
    contracts =relationship('Contract', backref='collaborater')
    
    def __repr__(self):
        return f'Collaborateur : {self.name}'