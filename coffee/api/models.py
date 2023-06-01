from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from api.manager import UserManager

# Create your models here.
class Roles(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)



class User(AbstractBaseUser):
    firstname = models.CharField(max_length=100)
    secondname = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=128)
    role = models.ForeignKey(Roles, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    object = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff
    
    def has_role(self, obj=None):
        return self.role