from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from utils.utils import Base
from models import contract


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    support_contact = Column(String(50))
    start_date = Column(Date())
    end_date = Column(Date())
    location = Column(String(100))
    Attendees = Column(String(10))
    notes = Column(String())
    
    contract_id = Column(Integer, ForeignKey('contract.id'))
