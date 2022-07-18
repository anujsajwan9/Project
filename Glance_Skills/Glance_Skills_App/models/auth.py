from django.db import models

from django.contrib.auth.models import User
from django.forms.widgets import NumberInput


class extendeduser(models.Model):
    user = models.OneToOneField(User,default=None,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    age = models.IntegerField(null=True,blank=True)
    profession = models.CharField(null=True,max_length=50)
    bio = models.CharField(null=True,max_length=256)
    image = models.ImageField(upload_to='images/user_images/',null=True , default = "/images/user_images/defaultuser.jpeg")

    def __str__(self):
        return self.user.username