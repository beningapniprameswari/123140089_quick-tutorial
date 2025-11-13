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