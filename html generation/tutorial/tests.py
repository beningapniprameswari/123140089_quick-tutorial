import unittest
from pyramid import testing

# --- UNIT TESTS (Menguji fungsi view secara langsung) ---
class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        # Impor dari file .views yang baru
        from .views import home

        request = testing.DummyRequest()
        response = home(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Visit', response.body)

    def test_hello(self):
        # Impor dari file .views yang baru
        from .views import hello

        request = testing.DummyRequest()
        response = hello(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Go back', response.body)

# --- FUNCTIONAL TESTS (Menguji seluruh aplikasi via URL) ---
class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from tutorial import main # Impor app factory
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_home(self):
        # Tes URL '/'
        res = self.testapp.get('/', status=200)
        self.assertIn(b'<body>Visit', res.body)

    def test_hello(self):
        # Tes URL '/howdy'
        res = self.testapp.get('/howdy', status=200)
        self.assertIn(b'<body>Go back', res.body)
        import unittest
from pyramid import testing

# --- UNIT TESTS (Menguji data yang dikembalikan view) ---
class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from .views import home

        request = testing.DummyRequest()
        # Panggil view function
        response = home(request) 
        
        # Cek apakah view mengembalikan DICTIONARY yang benar
        self.assertEqual('Home View', response['name'])

    def test_hello(self):
        from .views import hello

        request = testing.DummyRequest()
        # Panggil view function
        response = hello(request)
        
        # Cek apakah view mengembalikan DICTIONARY yang benar
        self.assertEqual('Hello View', response['name'])

# --- FUNCTIONAL TESTS (Menguji HTML yang sudah di-render) ---
class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from tutorial import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        # Cek apakah HTML AKHIR berisi data dari view
        self.assertIn(b'<h1>Hi Home View', res.body)

    def test_hello(self):
        res = self.testapp.get('/howdy', status=200)
        # Cek apakah HTML AKHIR berisi data dari view
        self.assertIn(b'<h1>Hi Hello View', res.body)