from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, default="")
    last_name = models.CharField(max_length=100, null=True, default="")
    address = models.CharField(max_length=50, null=True, default="")
    city = models.CharField(max_length=50, null=True, default="")
    state = models.CharField(max_length=50, null=True, default="")
    zip_code = models.CharField(max_length=50, null=True, default="")
    country = models.CharField(max_length=50, null=True, default="")
    
    def __str__(self):
        return f"{self.user} {self.first_name} {self.last_name}"