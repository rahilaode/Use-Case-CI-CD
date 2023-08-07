import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Selamat datang di halaman utama!')

    def test_about_page(self):
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)

        # Memastikan bahwa "about.html" ada dalam respon
        self.assertIn('about.html', response.data.decode())

        # Memastikan bahwa konten yang diharapkan ada dalam "about.html"
        expected_content = 'Tentang Kami'
        self.assertIn(expected_content, response.data.decode())

        # Memastikan bahwa konten lain yang diharapkan juga ada dalam "about.html"
        expected_author = 'Ditulis oleh John Doe'
        self.assertIn(expected_author, response.data.decode())

if __name__ == '__main__':
    unittest.main()
