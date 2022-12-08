import unittest
import requests
from .RejestrKont import RejestrKont


class ApiTest(unittest.TestCase):
    mock_name = "Dariusz"
    mock_surname = "Januszewski"
    mock_pesel = "12345678910"

    def setUp(self):
        RejestrKont.list = []

    def test_create_account_api(self):
        r = requests.post("http://127.0.0.1:5000/konta/stworz_konto",
                          json={'imie': self.mock_name, 'nazwisko': self.mock_surname, 'pesel': self.mock_pesel})
        self.assertEqual(r.status_code, 201)

    def test_get_created_account(self):
        r = requests.get(f"http://127.0.0.1:5000/konta/konto/{self.mock_pesel}", json={})
        print(r.json())
        self.assertEqual(r.json()['imie'], self.mock_name)
        self.assertEqual(r.json()['nazwisko'], self.mock_surname)

    def test_create_account_api_account_already_exists(self):
        r = requests.post("http://127.0.0.1:5000/konta/stworz_konto",
                          json={'imie': self.mock_name, 'nazwisko': self.mock_surname, 'pesel': self.mock_pesel})
        self.assertEqual(r.status_code, 400)

    def test_delete_account(self):
        r = requests.get(f"http://127.0.0.1:5000/konta/konto/delete/{self.mock_pesel}", json={})
        RejestrKont.delete(self.mock_pesel)
        self.assertEqual(RejestrKont.count(), 0)


    @classmethod
    def tearDown(cls):
        RejestrKont.list = []
