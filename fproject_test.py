import unittest

import fproject


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.app = unh698.app.test_client()

    def tearDown(self):
         pass

    def test_home_page(self):
        # Render the / path of the website
        rv = self.app.get('/')
        # Check that the page contains the desired phrase
        assert b'Continuous Development' in rv.data

if __name__ == '__main__':
    unittest.main()
