from django.db import models

# Create your models here.
from django.urls import reverse

class Product(models.Model):
     name = models.CharField(max_length=200)
     price = models.PositiveIntegerField()

     def __str__(self):
          return self.name
     
     #新規作成編集完了時のリダイレクト先
     def get_absolute_url(self):
          return reverse('list')