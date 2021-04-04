import unittest

from webapp import app

class SampleTestCase(unittest.TestCase):

    def test_response(self):
        tester = app.test_client(self)
        response = tester.get('/foundme')
        self.assertEqual(response.data, b'You found me!')

if __name__ == '__main__':
    unittest.main()
