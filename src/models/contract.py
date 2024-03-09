from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.utils.utils import Base


class Contract(Base):
    __tablename__ = "contract"

    id = Column(Integer, primary_key=True, unique=True)
    contract_price = Column(String(10))
    left_to_pay = Column(String(10))
    created_at = Column(Date())
    status = Column(Boolean(), default=False)
    events = relationship("Event", backref="contracts", uselist=False)
    collaborater_email = Column(String, ForeignKey("collaborater.email"))
    collaborater = relationship("Collaborater")
    customer_email = Column(String, ForeignKey("customer.email"))
    customer = relationship("Customer")

    def __repr__(self):
        return f"Contrat : {self.id}"
