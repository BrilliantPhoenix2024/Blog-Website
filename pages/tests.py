from django.test import TestCase

from django.contrib.auth.models import User
from django.shortcuts import reverse

from .models import My_design


class MyDesignTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='user1')
        cls.my_design1 = My_design.objects.create(
            title='Design1',
            description='this is some text for Design1',
            status=My_design.STATUS_CHOICES[0][0],  # published
            author=cls.user,
        )
        cls.my_design2 = My_design.objects.create(
            title='Design2',
            description='this is some text for Design2',
            status=My_design.STATUS_CHOICES[1][0],  # draft
            author=cls.user,
        )

    #
    # def setUp(self):


    def test_design_model_str(self):
        design = self.my_design1
        self.assertEqual(str(design), design.title)


    def test_design_detail(self):
        self.assertEqual(self.my_design1.title, 'Design1')
        self.assertEqual(self.my_design1.description, 'this is some text for Design1')


    def test_design_url(self):
        response = self.client.get('/design/')
        self.assertEqual(response.status_code, 200)


    def test_design_url_by_name(self):
        response = self.client.get(reverse('design'))
        self.assertEqual(response.status_code, 200)


    def test_design_title_on_design_page(self):
        response = self.client.get(reverse('design'))
        self.assertContains(response, 'Design1')


    def test_design_detail_url(self):
        response = self.client.get(f'/{self.my_design1.id}/')
        self.assertEqual(response.status_code, 200)


    def test_design_detail_url_by_name(self):
        response = self.client.get(reverse('detail_design', args=[self.my_design1.id]))
        self.assertEqual(response.status_code, 200)


    def test_design_detail_on_services_page(self):
        response = self.client.get('/1/')
        self.assertContains(response, self.my_design1.title)
        self.assertContains(response, self.my_design1.description)


    def test_design_detail_on_services_page(self):
        response = self.client.get(f'/{self.my_design1.id}/')
        self.assertContains(response, self.my_design1.title)
        self.assertContains(response, self.my_design1.description)


    def test_design_detail_on_services_page(self):
        response = self.client.get(reverse('detail_design', args=[self.my_design1.id]))
        self.assertContains(response, self.my_design1.title)
        self.assertContains(response, self.my_design1.description)


    def test_status_404_if_design_id_not_exist(self):
        response = self.client.get(reverse('detail_design', args=[999]))
        self.assertEqual(response.status_code, 404)


    def test_draft_design_not_show_in_design_list(self):
        response = self.client.get(reverse('design'))
        self.assertContains(response, self.my_design1.title)
        self.assertNotContains(response, self.my_design2.title)


    def test_design_create_view(self):
        response = self.client.post(reverse('create_design'), {
            'title': 'some title',
            'description': 'this is some text',
            'status': 'pub',
            'author': self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(My_design.objects.last().title, 'some title')
        self.assertEqual(My_design.objects.last().description, 'this is some text')


    def test_design_update_view(self):
        response = self.client.post(reverse('design_update', args=[self.my_design2.id]), {
            'title': 'Design2 updated',
            'description': 'this text is updated',
            'status': 'pub',
            'author': self.my_design2.author.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(My_design.objects.last().title, 'Design2 updated')
        self.assertEqual(My_design.objects.last().description, 'this text is updated')


    def test_design_delete_view(self):
        response = self.client.post(reverse('design_delete', args=[self.my_design2.id]))
        self.assertEqual(response.status_code, 302)
