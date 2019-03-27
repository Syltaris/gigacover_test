import psycopg2
import falcon
import api.customer as customer

"""
Create RESTful API endpoints so that we can make CRUD (create, read, update, delete) actions to the customers table. 
Then share Postman collection where we can use to make call to these endpoints.
"""

api = falcon.API()
api.add_route('/customer', customer.Customer())