import falcon
import json
from datetime import datetime
from models.customer import Customer as CustomerSchema

class Customer(object):
    """
    API object interfaces with PostgreSQL db to do CRUD ops on customer table.
    """
    def __init__(self, session):
        self.session = session()
    
    def __del__(self):
        self.session.close()

    def on_get(self, req, resp, id=None):
        if id is None:
            resp.status = falcon.HTTP_400
            return
        customer = self.session.query(CustomerSchema).filter(CustomerSchema.id == id).first()
        if customer is None:
            resp.body = "Customer not found"
            return
        payload = customer.to_json()
       
        resp.body = json.dumps(payload, ensure_ascii=False)

    def on_post(self, req, resp):
        data = json.loads(req.stream.read())
        dob = datetime.strptime(data['dob'], '%a %b %d %Y %H:%M:%S %Z%z')
        customer = CustomerSchema(name=data['name'], dob=dob)
        self.session.add(customer)
        self.session.commit()
        resp.body = json.dumps(customer.to_json(), ensure_ascii=False)

    def on_put(self, req, resp, id):
        if id is None:
            resp.status = falcon.HTTP_400
            return
        data = json.loads(req.stream.read())
        customer = self.session.query(CustomerSchema).filter(CustomerSchema.id == id).first()
        name = customer.name
        dob = customer.dob

        if 'name' in data:
            name = data['name']
        if 'dob' in data:
            dob = datetime.strptime(data['dob'], '%a %b %d %Y %H:%M:%S %Z%z')

        new_data = dict(name=name, dob=dob)
        self.session.query(CustomerSchema).filter(CustomerSchema.id == id).update(new_data)
        self.session.commit()

    def on_delete(self, req, resp, id):
        if id is None:
            resp.status = falcon.HTTP_400
            return
        self.session.query(CustomerSchema).filter(CustomerSchema.id==id).delete()
        self.session.commit()


    def retrieve_all_users(self):
        return self.session.query(CustomerSchema).all()
        
