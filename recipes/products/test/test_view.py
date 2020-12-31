from django.test import TestCase, Client
from django.urls import reverse

from products.models import (
    Grops,
    Simples,
)


class TestViewsGroup(TestCase):

    def setUp(self):
        self.clients = Client()
        self.list_groups = reverse('groups')
        self.group = Grops.objects.create(name='firtst group')

    def test_group_list(self):
        myresponse = self.clients.get(self.list_groups)
        self.assertEqual(myresponse.status_code, 200)

    def test_group_post(self):
        myresponse = self.clients.post(self.list_groups, {
            'name': 'second group',
            'razpad': 1
        })
        self.assertEqual(myresponse.status_code, 201)
        self.assertEqual(Grops.objects.all().count(), 2)


class TestViews(TestCase):

    def setUp(self):
        self.cliens = Client()
        self.list_urls = reverse('products')
        self.list_details_urls = reverse('products_detail', args=[1])

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

    def test_project_product_delete(self):
        Simples.objects.create(
            name='first item',
            quantity=1,
            group=self.group
        )
        myresponse = self.cliens.delete(self.list_details_urls)
        self.assertEqual(myresponse.status_code, 204)
        self.assertEqual(Simples.objects.all().count(), 0)
