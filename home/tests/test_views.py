from django.test import TestCase, Client

from django.urls import reverse
import json

class TestViews(TestCase):

    # General setups for the TestViews class
    def setUp(self):
        self.client = Client()
        self.index_url = '/'
        #self.results_url = reverse('/search_results', args=['physique'])

    # Test to see if Homepage response in the correct way
    def test_index_GET(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home_page.html')
    '''
        def test_search_results_GET(self):
        response = self.client.get(reverse('/search_results'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'results_page.html')
    '''


