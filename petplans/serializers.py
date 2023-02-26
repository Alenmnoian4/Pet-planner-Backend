from .models import Petplan
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our Petplan Serializer
class PetplanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Petplan
        # the fields that should be included in the serialized output
        fields = ['id', 'subject', 'details']