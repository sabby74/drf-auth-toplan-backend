from rest_framework import generics
from .models import Toplan
from rest_framework import permissions
from .serializers import ToplanSerializer

# Create your views here.

class ToplanList(generics.ListCreateAPIView):
    queryset = Toplan.objects.all()
    serializer_class = ToplanSerializer
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]


class ToplanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Toplan.objects.all()
    serializer_class = ToplanSerializer