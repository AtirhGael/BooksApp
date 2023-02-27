from django.db import models

# Create your models here.
class Books(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=10)
    isbn = models.CharField(max_length=10)

    # this is so that the title of a book will display in readable format in the admin
    def __str__(self):
        return self.title
