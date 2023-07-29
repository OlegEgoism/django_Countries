from rest_framework import serializers

from .models import Person, Organization


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = 'last_name', 'first_name', 'surname', 'photo', 'birthday', 'country', 'organization'


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = 'name',
