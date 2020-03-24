from django.shortcuts import render
from rest_framework import viewsets
from .models import Pasta
from .serializers import PastaSerializer

# Create your views here.

class PastaView(viewsets.ModelViewSet):
    queryset = Pasta.objects.all()
    serializer_class = PastaSerializer