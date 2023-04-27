from rest_framework import generics, permissions
from gear_addict_api.permissions import IsOwnerOrReadOnly
from .models import Rig
from .serializers import RigSerializer


class RigList(generics.ListCreateAPIView):
    """
    List rigs or create a rig if logged in
    The perform_create method associates the rig with the logged in user.
    """
    serializer_class = RigSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Rig.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RigDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a rig and edit or delete it if you own it.
    """
    serializer_class = RigSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Rig.objects.all()