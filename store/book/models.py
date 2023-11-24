from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publish_year = models.DateField()
    isbn = models.IntegerField(max_length=13)

    def __str__(self) -> str:
        return self.name