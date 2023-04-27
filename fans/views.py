from rest_framework import generics, permissions
from gear_addict_api.permissions import IsOwnerOrReadOnly
from fans.models import Fan
from fans.serializers import FanSerializer


class FanList(generics.ListCreateAPIView):
    """
    List all fans, i.e. all instances of user as a fan of
    another user.
    Create a fan, i.e. become a fan of a user if logged in
    perform_create: associate the current logged in user with a fan
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FanSerializer
    queryset = Fan.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FanDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a fan
    No Update view, as we either become a fan or unfan users
    Destroy a fan, i.e. unfan someone if owner
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FanSerializer
    queryset = Fan.objects.all()
