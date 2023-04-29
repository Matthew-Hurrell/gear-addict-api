from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from gear_addict_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    queryset = Profile.objects.annotate(
        rigs_count = Count('owner__rig', distinct=True),
        fans_count = Count('owner__idolguy', distinct=True),
        idols_count = Count('owner__fanboy', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        # Profiles following a User
        'owner__fanboy__idol__profile'
    ]
    ordering_fields = [
        'rigs_count',
        'fans_count',
        'idols_count',
        'owner__fanboy__created_at',
        'owner__idolguy__created_at',
    ]

class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        rigs_count = Count('owner__rig', distinct=True),
        fans_count = Count('owner__idolguy', distinct=True),
        idols_count = Count('owner__fanboy', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer