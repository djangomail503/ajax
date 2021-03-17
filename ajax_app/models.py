from django.db import models

# Create your models here.
class MyUser(models.Model):

    username = models.CharField(max_length=256, unique = True)
    name = models.CharField(max_length=256)
    email = models.EmailField()
    link = models.URLField()

    def __str__(self):
        return self.username


        
        