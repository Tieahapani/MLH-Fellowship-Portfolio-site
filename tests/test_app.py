import os
import unittest

os.environ['TESTING'] = 'true'

from app import app, myportfoliodb, TimelinePost

class AppTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        myportfoliodb.connect(reuse_if_open=True)
        myportfoliodb.create_tables([TimelinePost])

    @classmethod
    def tearDownClass(cls):
        myportfoliodb.drop_tables([TimelinePost])
        if not myportfoliodb.is_closed():
            myportfoliodb.close()

    def setUp(self):
        TimelinePost.delete().execute()
        self.client = app.test_client()
    
    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "About Me" in html
        assert "Volunteer Workflow Automation Assistant" in html
        assert "San Francisco State University" in html
        # Tests navbar
        assert "/timeline" in html
