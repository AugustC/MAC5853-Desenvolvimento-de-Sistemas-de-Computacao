import unittest, os, json
import http.client
from .. import create_app, db, resources

class URLTestCase(unittest.TestCase):

    def setUp(self):
        #TODO change to test name
        self.app = create_app()
        self.client = self.app.test_client
        self.url = {'urlpath': 'www.google.com'}
        with self.app.app_context():
            db.create_all()

    def testURLCreation(self):
        res = self.client().post('/url', data=self.url)
        self.assertEqual(res.status_code, 201)
        self.assertIn('www.google.com', str(res.data))

