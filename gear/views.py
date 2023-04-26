from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Gear
from .serializers import GearSerializer
from gear_addict_api.permissions import IsOwnerOrReadOnly


class GearList(APIView):
    serializer_class = GearSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        gear = Gear.objects.all()
        serializer = GearSerializer(
            gear, 
            many = True,
            context = {'request': request}
        )
        return Response(serializer.data)
    
    def post(self, request):
        serializer = GearSerializer(
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


class GearDetail(APIView):
    serializer_class = GearSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def get_object(self, pk):
        try: 
            gear = Gear.objects.get(pk=pk) 
            self.check_object_permissions(self.request, gear)
            return gear
        except Gear.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        gear = self.get_object(pk) 
        serializer=GearSerializer(
            gear,
            context= {'request' : request}
        ) 
        return Response(serializer.data)
    
    def put(self, request, pk):
        gear = self.get_object(pk)
        serializer=GearSerializer(
            gear,
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
        gear = self.get_object(pk)
        gear.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
