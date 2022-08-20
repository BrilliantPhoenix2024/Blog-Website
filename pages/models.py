from django.shortcuts import reverse
from django.db import models

class My_design(models.Model):
    STATUS_CHOICES = (
        ('pub', 'Published'),
        ('drf', 'Draft'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_design', args=[self.id])


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    msg = models.TextField()

    def __str__(self):
        return self.name




