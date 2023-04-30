from rest_framework import generics, permissions
from gear_addict_api.permissions import IsOwnerOrReadOnly
from save.models import Save
from save.serializers import SaveSerializer


class SaveList(generics.ListCreateAPIView):
    """
    List saves or add save if logged in
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SaveSerializer
    queryset = Save.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SaveDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a save. No Update view, as users can
    only save or unsave a post. Destroy a save,
    i.e. unsave a post if owner of that save
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SaveSerializer
    queryset = Save.objects.all()
