import unittest, os, json
import http.client
from .. import create_app, db, resources

class StatusTypeTestCase(unittest.TestCase):

    def setUp(self):
        #TODO change to test name
        self.app = create_app()
        self.client = self.app.test_client
        self.description_creation= json.dumps(dict(description='Status Type 1'))
        self.description_find = json.dumps(dict(description='Status Type 2'))
        self.description_delete = json.dumps(dict(description='Status Type 3'))
        with self.app.app_context():
            db.create_all()

    def prepareStatusType(self, description):
        rv = self.client().post('/status_type', data=description, content_type='application/json')
        return rv.json.get('id')

    def testCreation(self):
        res = self.client().post('/status_type', data=self.description_creation, content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn('Status Type 1', str(res.data))

    def testFind(self):
        id = self.prepareStatusType(self.description_find)
        jsonid = json.dumps(dict(id=id, description=self.description_find))
        res = self.client().get('/status_type', data=jsonid, content_type='application/json')
        self.assertIn(str(id), str(res.json.get('id')))

    def testDelete(self):
        id = self.prepareStatusType(self.description_delete)
        jsonid = json.dumps(dict(id=id, description=self.description_delete))
        res = self.client().delete('/status_type', data=jsonid, content_type='application/json')
        self.assertEqual(res.status_code, 200)