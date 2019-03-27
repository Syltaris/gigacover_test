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

    def on_put(self, req, resp):
        doc = {
            'sg': 'oof'
        }
        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp):
        doc = {
            'sg': 'owie'
        }
        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200

    def retrieve_all_users(self):
        return self.session.query(CustomerSchema).all()
        
