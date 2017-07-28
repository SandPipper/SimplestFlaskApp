import unittest
import json
from app.models import SimpleModel
from app import app, db


class BasicTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/index', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_add_string(self):
        with app.app_context():
            tester = app.test_client(self)
            response = tester.post('/form', data=dict(inputer="UnitTest"))
            data = json.loads((response.data).decode('utf-8'))
            self.assertEqual(data['status'], 1)
            db.session.query(SimpleModel).filter_by(string="UnitTest").delete()
            db.session.commit()

if __name__ == "__main__":
    unittest.main()
