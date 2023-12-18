from django.shortcuts import render
from rest_framework import viewsets
from . models import student
from . serializers import studentSerializers

# Create your views here.

class studentViewsets(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = studentSerializers