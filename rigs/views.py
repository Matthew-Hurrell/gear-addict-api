from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
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
    queryset = Rig.objects.annotate(
        comments_count = Count('comment', distinct=True),
        likes_count = Count('likes', distinct=True),
        saves_count = Count('save', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        # User feed
        'owner__idolguy__fan__profile',
        # User liked rigs
        'likes__owner__profile',
        # User rigs
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'category',
        'attributes',
        'genre',
    ]
    ordering_fields = [
        'comments_count',
        'likes_count',
        'saves_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RigDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a rig and edit or delete it if you own it.
    """
    serializer_class = RigSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Rig.objects.annotate(
        comments_count = Count('comment', distinct=True),
        likes_count = Count('likes', distinct=True),
        saves_count = Count('save', distinct=True),
    ).order_by('-created_at')