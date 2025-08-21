from django.db import models
from users.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username
