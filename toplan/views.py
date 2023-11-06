from rest_framework import generics
from .models import Toplan
from .serializers import ToplanSerializer

# Create your views here.

class ToplanList(generics.ListCreateAPIView):
    queryset = Toplan.objects.all()
    serializer_class = ToplanSerializer


class ToplanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Toplan.objects.all()
    serializer_class = ToplanSerializer