from django.db import models
from users.models import User

class TextItem(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="texts")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
