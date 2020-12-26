from django.http import response
from django.test import TestCase, Client
from products.views import (
    SimpleListView,
    GroupListView,
    RecepiListView,
    RecepiDetails,
    RecepiIng,
    RecepiIngDetail
)
from django.urls import reverse
from products.models import (
    Grops,
    Simples,
    RecipeIngredient,
    Recepies
)
import json


class TestViews(TestCase):

    def setUp(self):
        self.cliens = Client()
        self.list_urls = reverse('products')
        self.list_details_urls = reverse('recepi_detail', args=[1])

        self.group = Grops.objects.create(name='firtst group')

    def test_project_product_list(self):
        myresponse = self.cliens.get(self.list_urls)
        self.assertEqual(myresponse.status_code, 200)

    def test_project_product_post(self):
        myresponse = self.cliens.post(self.list_urls, {
            'name': 'first product',
            'quantity': 1,
            'group': self.group.pk
        })
        self.assertEqual(myresponse.status_code, 201)
        self.assertEqual(Grops.objects.get(pk=1).name, 'firtst group')
        self.assertEqual(Simples.objects.get(pk=1).group.name, 'firtst group')
        self.assertEqual(Simples.objects.filter(name='first product')[0].group.name, 'firtst group')
