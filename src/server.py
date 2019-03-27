import falcon
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api import customer as customer
from models.base import Base

"""
Create RESTful API endpoints so that we can make CRUD (create, read, update, delete) actions to the customers table. 
Then share Postman collection where we can use to make call to these endpoints.

NOTE: for the simple purpose of the exercise, the username:password is hardcoded into the string.
It is more preferable to put these into a .env file to be supplied by each individual instead.
"""
api = falcon.API()
#conn = psycopg2.connect("dbname=testdb user=postgres")
engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/testdb", echo=True)
Session = sessionmaker(bind=engine)
conn = engine.connect()
api.add_route('/customer/{id}', customer.Customer(Session))

Base.metadata.create_all(engine)