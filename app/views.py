import models
from rest_framework import viewsets
import serializers

# Create your views here.

class blog(viewsets.ModelViewSet):
	serializer_class = serializers.serializer_wpisu
	queryset = models.wpis.objects.all()
