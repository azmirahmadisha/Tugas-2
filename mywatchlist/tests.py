from django.test import TestCase, Client
from django.urls import resolve

# Create your tests here.

class TestingWatchlist(TestCase):
    def testing_app_url(self):
        response = self.client.get('/mywatchlist/')
        self.assertEqual(response.status_code,200)

    def testing_app_url_json(self):
        response = self.client.get('/mywatchlist/json/')
        self.assertEqual(response.status_code,200)

    def testing_app_url_xml(self):
        response = self.client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)

    def testing_app_url_html(self):
        response = self.client.get('/mywatchlist/html/')
        self.assertEqual(response.status_code,200)


        