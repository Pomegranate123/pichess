from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Online(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    online = models.BooleanField()
