import os

from flask_testing import TestCase

from add2numbers import create_app


class TestBase(TestCase):
    """
    Create app with sqlite database
    """
    def create_app(self):
        app = create_app()
        return app

    def setUp(self):
        """
        Before each test
        """
        self.client = self.app.test_client()
        self.client.testing = True

    def tearDown(self):
        """
        After each test
        """
        pass