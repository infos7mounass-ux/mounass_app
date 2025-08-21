from rest_framework import serializers
from .models import TextItem

class TextItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextItem
        fields = "__all__"
