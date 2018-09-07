from django.shortcuts import render

from django.contrib.auth.models import User, Group

from .models import Person

from rest_framework import viewsets

from quickstart.serializer import UserSerializer, GroupSerializer, PersonSerializer


class UserViewSet(viewsets.ModelViewSet):
    """

    API endpoint that allows users to be viewed or edited.

    """

    queryset = User.objects.all()

    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """

    API endpoint that allows groups to be viewed or edited.

    """

    queryset = Group.objects.all()

    serializer_class = GroupSerializer


class PersonViewSet(viewsets.ModelViewSet):

    queryset = Person.objects.all()

    serializer_class = PersonSerializer