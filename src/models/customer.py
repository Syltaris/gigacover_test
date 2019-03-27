from sqlalchemy import Column, Integer, String, DateTime
from .base import Base

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

  def __repr___(self):
      return "<Customer(name='%s', dob='%s')>" % (self.name, self.dob)
