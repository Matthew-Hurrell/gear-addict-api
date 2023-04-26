from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Rig
from .serializers import RigSerializer
from gear_addict_api.permissions import IsOwnerOrReadOnly


class RigList(APIView):
    serializer_class = RigSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        rigs = Rig.objects.all()
        serializer = RigSerializer(
        rigs, many = True, context = {'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = RigSerializer(
            data=request.data,
            context ={'request':request} 
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class RigDetail(APIView):
    serializer_class = RigSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def get_object(self, pk):
        try: 
            rig = Rig.objects.get(pk=pk) 
            self.check_object_permissions(self.request, rig)
            return rig
        except Rig.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        rig = self.get_object(pk) 
        serializer=RigSerializer(
            rig,
            context= {'request' : request}
        ) 
        return Response(serializer.data)
    
    def put(self, request, pk):
        rig = self.get_object(pk)
        serializer=RigSerializer(
            rig,
            data=request.data,
            context= {'request' : request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        rig = self.get_object(pk)
        rig.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
