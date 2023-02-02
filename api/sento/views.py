from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Area, Sento, UserSentoVisit
from .serializers import AreaSerializer, SentoSerializer, UserSentoVisitSerializer, UserSentoVisitPostDeleteSerializer


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


@api_view(['GET', 'POST', 'DELETE'])
def sento_visit_list(request):
    if request.method == 'GET':
        permission_classes = [IsAuthenticated]
        visits = UserSentoVisit.objects.filter(user_id=request.user.id)
        serializer = UserSentoVisitSerializer(visits, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    if request.method == 'POST':
        permission_classes = [IsAuthenticated]
        serializer = UserSentoVisitPostDeleteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        permission_classes = [IsAuthenticated]
        serializer = UserSentoVisitPostDeleteSerializer(data=request.data)
        if serializer.is_valid():
            sento_id = serializer.data['sento']
            user_id = serializer.data['user']
            sento = UserSentoVisit.objects.filter(user_id=user_id, sento_id=sento_id)
            sento.delete()
            return Response(serializer.data, status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors)
