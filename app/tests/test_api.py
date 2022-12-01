import unittest
import requests


class ApiTest(unittest.TestCase):
    mock_name = "Dariusz"
    mock_surname = "Januszewski"
    mock_pesel = "12345678910"

    def test_create_account_api(self):
        r = requests.post("http://127.0.0.1:5000/konta/stworz_konto", json={'imie': self.mock_name, 'nazwisko': self.mock_surname, 'pesel': self.mock_pesel})
        self.assertEqual(r.status_code, 201)

    def test_get_created_account(self):
        r = requests.get(f"http://127.0.0.1:5000/konta/konto/{self.mock_pesel}")
        print(r.text)
        pass