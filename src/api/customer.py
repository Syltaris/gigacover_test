import falcon
import json

class Customer(object):
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
        doc = {
            'sg': 'ah'
        }
        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200