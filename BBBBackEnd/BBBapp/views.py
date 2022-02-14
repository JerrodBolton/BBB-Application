from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import BBBSerializer
from .models import BBBCatalog

# maybe: readList 
class BBBList(generics.ListAPIView):# If I have list that means that I don't need a ID  in the  endPoint
    queryset = BBBCatalog.objects.all()
    serializer_class = BBBSerializer

# The postDetail needs the same things
# TODO:change the naming to something more conventional 
# maybe: readDetail