from rest_framework import generics, permissions
from gear_addict_api.permissions import IsOwnerOrReadOnly
from stars.models import Star
from stars.serializers import StarSerializer


class StarList(generics.ListCreateAPIView):
    """
    List stars or add star if logged in
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StarSerializer
    queryset = Star.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StarDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a star. No Update view, as users can
    only star or unstar a rig. Destroy a star,
    i.e. unstar a rig if owner of that star
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = StarSerializer
    queryset = Star.objects.all()
