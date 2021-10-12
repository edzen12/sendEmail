from rest_framework import viewsets, mixins

from contact.models import Person
from contact.serializers import PersonSerializer


class PersonViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
