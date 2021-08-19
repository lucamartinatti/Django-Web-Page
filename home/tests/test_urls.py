from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import index, search_results

class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_serch_results_url_resolves(self):
        url = reverse('search-results')
        self.assertEquals(resolve(url).func, search_results)