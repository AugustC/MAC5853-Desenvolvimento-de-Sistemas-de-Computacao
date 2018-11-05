import unittest, os, json
import http.client
from .. import create_app, db, resources

class URLTestCase(unittest.TestCase):

    def setUp(self):
        #TODO change to test name
        self.app = create_app()
        self.client = self.app.test_client
        self.url_creation = json.dumps(dict(urlpath='www.googlecreation.com'))
        self.url_find = json.dumps(dict(urlpath='www.googlefind.com'))
        self.url_delete = json.dumps(dict(urlpath='www.googledelete.com'))
        with self.app.app_context():
            db.create_all()

    def prepareUrl(self, url):
        rv =self.client().get('url', data=url, content_type='application/json')
        if (rv.status_code == 202):
            rv = self.client().delete('/url', data=url, content_type='application/json')

    def testURLCreation(self):
        self.prepareUrl(self.url_creation)
        res = self.client().post('/url', data=self.url_creation, content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn('www.googlecreation.com', str(res.data))

    def testURLFind(self):
        self.prepareUrl(self.url_find)
        rv = self.client().post('/url', data=self.url_find, content_type='application/json')
        res = self.client().get('/url', data=self.url_find, content_type='application/json')
        self.assertEqual('www.googlefind.com', str(res.json.get('urlpath')))

    def testURLDelete(self):
        self.prepareUrl(self.url_delete)
        rv = self.client().post('/url', data=self.url_delete, content_type='application/json')
        res = self.client().delete('/url', data=self.url_delete, content_type='application/json')
        self.assertEqual(res.status_code, 200)