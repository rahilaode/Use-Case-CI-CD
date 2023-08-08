import unittest
import requests
from app import app

class TestApp(unittest.TestCase):
    URL = "http://127.0.0.1:5000"
    
    # Fungsi untuk mencek halaman home
    def home_url(self):
        print("=======================")
        print("HOME URL TESTING")
        print("=======================")
        
        # Mendapatkan respon
        resp = requests.get(self.URL)
        
        # Cek apakah ada respon atau tidak
        self.assertEqual(resp.status_code, 200, "No response from HOME URL")
        print("Test 1 Passed")
        
        # Cek isi konten dari respon
        self.assertAlmostEqual(resp._content, b'Selamat datang di halaman utama!')
        print("Test 2 Passed\n")
        
        print("Testing for HOME URL ARE SUCCESFULLY PASSED !!!\n")
        
    def about_url(self):
        print("=======================")
        print("ABOUT URL TESTING")
        print("=======================")
        URL = self.URL + "/about"
        
        # Mendapatkan respon
        resp = requests.get(URL)
        
        # Cek apakah ada respon atau tidak
        self.assertEqual(resp.status_code, 200, "No response from ABOUT URL")
        print("Test 1 Passed")
        
        # Cek isi konten dari respon
        self.assertIn('Tentang Kami', resp.text)
        print("Test 2 Passed")
        
        # Cek isi konten dari respons
        self.assertIn('Aplikasi ini memberikan estimasi harga rumah berdasarkan fitur-fitur tertentu.', resp.text)
        self.assertIn('Tim kami berkomitmen untuk memberikan informasi yang akurat dan berguna bagi pengguna kami.', resp.text)
        self.assertIn('Ditulis oleh John Doe', resp.text)
        print("Test 3 Passed\n")
        
        print("Testing for ABOUT URL ARE SUCCESFULLY PASSED !!!\n")
        
if __name__ == '__main__':
    tester = TestApp()
    tester.home_url()
    tester.about_url()