from .models import Petplan
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PetplanSerializer


class PetplanViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Petplan.objects.all()
    # The serializer class for serializing output
    serializer_class = PetplanSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]