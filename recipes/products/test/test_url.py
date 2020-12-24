from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import (
    SimpleListView,
    GroupListView,
    RecepiListView,
    RecepiDetails,
    RecepiIng,
    RecepiIngDetail
)


class TestUrls(SimpleTestCase):

    def test_products_url_is_resolve(self):
        url = reverse('products')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, SimpleListView)

    def test_groups_url_is_resolve(self):
        url = reverse('groups')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, GroupListView)

    def test_recepi_url_is_resolve(self):
        url = reverse('recepi')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, RecepiListView)

    def test_recepi_detail_url_is_resolve(self):
        url = reverse('recepi_detail', args=[1])
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, RecepiDetails)

    def test_recepiing_url_is_resolve(self):
        url = reverse('recepiing')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, RecepiIng)

    def test_recepiing_retail_is_resolve(self):
        url = reverse('recepiing_detail', args=[1])
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, RecepiIngDetail)
