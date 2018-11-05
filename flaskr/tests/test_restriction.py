import unittest, os, json
import http.client
from .. import create_app, db, resources

class RestrictionTestCase(unittest.TestCase):

    def setUp(self):
        #TODO change to test name
        self.app = create_app()
        self.client = self.app.test_client
        self.description_creation= json.dumps(dict(description='Restriction 1'))
        self.description_find = json.dumps(dict(description='Restriction 2'))
        self.description_delete = json.dumps(dict(description='Restriction 3'))
        with self.app.app_context():
            db.create_all()

    def prepareResriction(self, description):
        rv = self.client().post('/restriction', data=description, content_type='application/json')
        return rv.json.get('id')

    def testCreation(self):
        res = self.client().post('/restriction', data=self.description_creation, content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn('Restriction 1', str(res.data))

    def testFind(self):
        id = self.prepareResriction(self.description_find)
        jsonid = json.dumps(dict(id=id, description=self.description_find))
        res = self.client().get('/restriction', data=jsonid, content_type='application/json')
        self.assertIn(str(id), str(res.json.get('id')))

    def testDelete(self):
        id = self.prepareResriction(self.description_delete)
        jsonid = json.dumps(dict(id=id, description=self.description_delete))
        res = self.client().delete('/restriction', data=jsonid, content_type='application/json')
        self.assertEqual(res.status_code, 200)