from django.db import models
from django.contrib.auth.models import User


#AbstractUser model for customized user model
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES=[
        ('Super admin', 'Super admin'),
        ('Admin', 'Admin'),
        ('User', 'User'),
    ]
    user_type=models.CharField(max_length=20,choices=ROLES)

    def __str__(self):
        return self.user_type

class UserAccess(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    can_edit=models.BooleanField(default=False)
    can_view=models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)



