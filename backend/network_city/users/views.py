from rest_framework import generics
from .models import Users
from serialisers import UserstSerialiser

class UsersList(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserstSerialiser