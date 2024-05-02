from django.db import models


from django.contrib.auth.models import User
class userreg(models.Model):
    username = models.CharField(max_length=20, unique=True )
    email = models.EmailField(max_length=100 ,unique=True)
    password = models.CharField(max_length=20)

    def class_name(self):
        return self.__class__.__name__