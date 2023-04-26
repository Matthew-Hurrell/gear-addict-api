from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Gear
from .serializers import GearSerializer


class GearList(APIView):
    def get(self, request):
        gear = Gear.objects.all()
        serializer = GearSerializer(
            gear, many = True, context = {'request': request}
        )
        return Response(serializer.data)
