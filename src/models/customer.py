from sqlalchemy import Column, Integer, String, DateTime
from .base import Base
from datetime import datetime

class Customer(Base):
  """
  customers(
    id (autoincrease), 
    name str, 
    dob date, 
    updated_at timestamp
  ) 
  """
  __tablename__ = 'customer'

  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String)
  dob = Column(DateTime)
  updated_at = Column(DateTime)

  def __init__(self, name, dob):
    self.name = name
    self.dob = dob
    self.updated_at = datetime.now()

  def to_json(self):
    return dict(id=self.id, name=self.name, dob=str(self.dob), updated_at=str(self.updated_at))