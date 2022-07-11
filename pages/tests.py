from django.test import TestCase

from django.contrib.auth.models import User
from django.shortcuts import reverse

from .models import My_design

class MyDesignTest(TestCase):
   def setUp(self):
       self.user = User.objects.create(username='user1')
       self.my_design1 = My_design.objects.create(
           title='Design1',
           description='this is some text for Design1',
           status='My_design.STATUS_CHOICES[0]',
           author=self.user,
       )

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
       response = self.client.get(reverse('services', args=[self.my_design1.id]))
       self.assertEqual(response.status_code, 200)


   # def test_design_detail_on_services_page(self):
   #     response = self.client.get('/1/')
   #     self.assertContains(response, self.my_design1.title)
   #     self.assertContains(response, self.my_design1.description)

   def test_design_detail_on_services_page(self):
       response = self.client.get(f'/{self.my_design1.id}/')
       self.assertContains(response, self.my_design1.title)
       self.assertContains(response, self.my_design1.description)

   def test_design_detail_on_services_page(self):
       response = self.client.get(reverse('services', args=[self.my_design1.id]))
       self.assertContains(response, self.my_design1.title)
       self.assertContains(response, self.my_design1.description)

   def test_status_404_if_design_id_not_exist(self):
       response = self.client.get(reverse('services', args=[999]))
       self.assertEqual(response.status_code, 404)














