import unittest
from pyramid import testing

class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        # setUp() membuat environment Pyramid minimal
        self.config = testing.setUp()

    def tearDown(self):
        # tearDown() membersihkan environment setelah tes selesai
        testing.tearDown()

    def test_hello_world(self):
        # Impor view function yang mau dites
        from tutorial import hello_world

        # Buat request tiruan (DummyRequest)
        request = testing.DummyRequest()
        
        # Panggil view function secara langsung
        response = hello_world(request)
        
        # Cek apakah status code-nya 200 (OK)
        self.assertEqual(response.status_code, 200)

import unittest
from pyramid import testing

# --- INI ADALAH TES DARI TUTORIAL 05 ---
class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_hello_world(self):
        from tutorial import hello_world

        request = testing.DummyRequest()
        response = hello_world(request)
        self.assertEqual(response.status_code, 200)

# --- INI ADALAH TES BARU UNTUK TUTORIAL 06 ---
class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from tutorial import main  # Impor app factory
        app = main({})             # Buat aplikasi yang "sebenarnya"
        from webtest import TestApp

        # Bungkus aplikasi dengan 'TestApp'
        self.testapp = TestApp(app) 

    def test_hello_world(self):
        # Lakukan GET request tiruan ke URL '/'
        res = self.testapp.get('/', status=200) 
        
        # Cek apakah body HTML-nya berisi string yang kita harapkan
        self.assertIn(b'<h1>Hello World!</h1>', res.body)