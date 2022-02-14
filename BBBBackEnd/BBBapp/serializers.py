from rest_framework import serializers
from .models import BBBCatalog

class BBBSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','author','title','body','created_at')
        model = BBBCatalog