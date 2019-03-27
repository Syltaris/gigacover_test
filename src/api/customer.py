import falcon
import json
from models import customer as CustomerSchema

class Customer(object):
    """
    API object interfaces with PostgreSQL db to do CRUD ops on customer table.
    """
    def __init__(self, db_cur):
        self.db_cur = db_cur
    
    def __del__(self):
        if not self.db_cur.closed:
            self.db_cur.close()

    def on_get(self, req, resp):
        doc = {
            'sg': 'eek'
        }
        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200

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

    def on_post(self, req, resp):
        #self.cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
        #self.cur.commit()
        doc = {
            'sg': 'ah'
        }
        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200