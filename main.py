import falcon
import json
import requests
from kyuko import fetchKyukoInfo

class KyukoResource:

    def on_get(self, req, resp):
        kyuko = fetchKyukoInfo()
        resp.body = json.dumps([x.to_dict() for x in kyuko])


app = falcon.API()
app.add_route('/api/kyuko', KyukoResource())
