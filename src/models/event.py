from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.utils.utils import Base


class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(100))
    start_date = Column(Date())
    end_date = Column(Date())
    location = Column(String(100))
    attendees = Column(String(10))
    notes = Column(String())
    contract_id = Column(Integer, ForeignKey("contract.id"))
    contract = relationship("Contract")
    customer_email = Column(String, ForeignKey("customer.email"))
    customer = relationship("Customer")
    support_contact = Column(String, ForeignKey("collaborater.email"))
    collaborater = relationship("Collaborater")

    def __repr__(self):
        return f"Evènement : {self.name}"
