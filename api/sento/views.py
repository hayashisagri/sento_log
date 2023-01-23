from rest_framework import status, views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Area, Sento
from .serializers import AreaSerializer, SentoSerializer


@api_view()
def area_list(request):
    areas = Area.objects.all()
    permission_classes = [AllowAny]
    serializer = AreaSerializer(areas, many=True)
    return Response(serializer.data, status.HTTP_200_OK)


@api_view()
def area_details(request, pk):
    sento = Sento.objects.get(pk=pk)
    permission_classes = [AllowAny]
    serializer = SentoSerializer(sento)
    return Response(serializer.data, status.HTTP_200_OK)


@api_view()
def sento_list(request):
    sentos = Sento.objects.all()
    permission_classes = [AllowAny]
    serializer = SentoSerializer(sentos, many=True)
    return Response(serializer.data, status.HTTP_200_OK)


@api_view()
def sento_details(request, pk):
    sento = Sento.objects.get(pk=pk)
    permission_classes = [AllowAny]
    serializer = SentoSerializer(sento)
    return Response(serializer.data, status.HTTP_200_OK)
