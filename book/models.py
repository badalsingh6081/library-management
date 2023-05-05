from django.db import models

# Create your models here.


class book(models.Model):
    title=models.CharField(max_length=70)
    author=models.CharField(max_length=70)
    publisher=models.CharField(max_length=70)
    publish_date=models.DateField()
    category=models.CharField(max_length=70)



