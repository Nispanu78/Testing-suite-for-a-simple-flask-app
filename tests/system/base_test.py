from unittest import TestCase
from app import app

class BaseTest(TestCase):
    def setUp(self):
        app.Testing = True
        self.app = app.test_client