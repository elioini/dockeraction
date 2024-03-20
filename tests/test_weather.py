import unittest
from app import app

class TestWeatherApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_weather_valid_city(self):
        response = self.app.get('/weather?city=London')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIn('city', data)
        self.assertIn('temperature', data)
        self.assertIn('description', data)

    def test_get_weather_missing_city(self):
        response = self.app.get('/weather')
        self.assertEqual(response.status_code, 400)
        data = response.json
        self.assertIn('error', data)

    def test_get_weather_invalid_city(self):
        response = self.app.get('/weather?city=NonExistentCity')
        self.assertEqual(response.status_code, 404)
        data = response.json
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()

