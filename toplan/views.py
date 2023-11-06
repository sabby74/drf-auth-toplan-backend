from .models import Toplan
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ToplanSerializer


class ToplanViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Toplan.objects.all()
    # The serializer class for serializing output
    serializer_class = ToplanSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]