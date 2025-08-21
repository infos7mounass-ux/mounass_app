from rest_framework import viewsets
from .models import TextItem
from .serializers import TextItemSerializer

class TextItemViewSet(viewsets.ModelViewSet):
    queryset = TextItem.objects.all()
    serializer_class = TextItemSerializer
