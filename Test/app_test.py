import app
import unittest


class TestHealthEndpoint(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def test_main_page(self):
        response = self.app.get('/_health')
        print(response)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
