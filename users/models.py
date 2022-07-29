from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null =True,blank=True)
    profile_pix = models.ImageField(upload_to="profile")
    registered = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return self.full_name