from rest_framework import viewsets
from conf.serializers import PersonSerializer, OrganizationSerializer
from .models import Person, Organization


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
