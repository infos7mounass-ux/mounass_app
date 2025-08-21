from django.db import models
from users.models import User

class Property(models.Model):
    PROPERTY_TYPES = (
        ("rent", "For Rent"),
        ("sale", "For Sale"),
    )

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    type = models.CharField(max_length=10, choices=PROPERTY_TYPES)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="properties")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
