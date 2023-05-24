from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from gear_addict_api.permissions import IsOwnerOrReadOnly
from .models import Gear
from .serializers import GearSerializer


class GearList(generics.ListCreateAPIView):
    """
    List gear or create gear if logged in
    The perform_create method associates the gear with the logged in user.
    """
    serializer_class = GearSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Gear.objects.all()
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        # User gear
        'owner__profile',
    ]
    search_fields = [
        'name',
        'category',
        'brand',
        'model',
        'description',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GearDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve gear and edit or delete it if you own it.
    """
    serializer_class = GearSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Gear.objects.all()
