import unittest

import fproject


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.app = fproject.app.test_client()

    def tearDown(self):
         pass

    def test_home_page(self):
        # Render the / path of the website
        rv = self.app.get('/')
        # Check that the page contains the desired phrase
        assert b'Continuous Development' in rv.data

    def test_cloud_page(self):
        # Render the / path of the website
        rv = self.app.get('/cloud')
        # Check that the page contains the desired phrase
        assert b'The Use of The Cloud In Continuous Development' in rv.data

    def test_best_page(self):
        # Render the / path of the website
        rv = self.app.get('/best')
        # Check that the page contains the desired phrase
        assert b'Best Practices In Continuous Development' in rv.data

if __name__ == '__main__':
    unittest.main()
