import unittest, os, json
import http.client
from .. import create_app, db, resources

class ProhibitionTypeTestCase(unittest.TestCase):

    def setUp(self):
        #TODO change to test name
        self.app = create_app()
        self.client = self.app.test_client
        self.description_creation= json.dumps(dict(description='Prohibition Type 1'))
        self.description_find = json.dumps(dict(description='Prohibition Type 2'))
        self.description_delete = json.dumps(dict(description='Prohibition Type 3'))
        with self.app.app_context():
            db.create_all()

    def prepareProhibitionType(self, description):
        rv = self.client().post('/prohibition_type', data=description, content_type='application/json')
        return rv.json.get('id')

    def testCreation(self):
        res = self.client().post('/prohibition_type', data=self.description_creation, content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn('Prohibition Type 1', str(res.data))

    def testFind(self):
        id = self.prepareProhibitionType(self.description_find)
        jsonid = json.dumps(dict(id=id, description=self.description_find))
        res = self.client().get('/prohibition_type', data=jsonid, content_type='application/json')
        self.assertIn(str(id), str(res.json.get('id')))

    def testDelete(self):
        id = self.prepareProhibitionType(self.description_delete)
        jsonid = json.dumps(dict(id=id, description=self.description_delete))
        res = self.client().delete('/prohibition_type', data=jsonid, content_type='application/json')
        self.assertEqual(res.status_code, 200)