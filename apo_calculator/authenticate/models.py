from django.db import models
from django.contrib import auth

# Create your models here.
#We use the built-in User Model and add PermissionsMixins
class User(auth.models.User, auth.models.PermissionsMixin):

    #print method that prints out @UserName.
    def __str__(self):
        return "@{}".format(self.username)
