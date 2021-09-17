from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    password = models.CharField( max_length=50)
    address = models.TextField()
    created_on = models.TimeField( auto_now_add=True)

    def __str__(self):
        return self.username
    
