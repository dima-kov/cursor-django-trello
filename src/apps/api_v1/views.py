from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


@api_view(http_method_names=['GET'])
def check(request):
    return Response(data={"status": 'OK'}, status=status.HTTP_200_OK)


class HealthcheckView(APIView):
    def get(self, request):
        return Response(data={"status": 'OK'}, status=status.HTTP_200_OK)


@api_view(http_method_names=['GET'])
@permission_classes([IsAuthenticated])
def test_django_sessions_view(request):

    return Response({}, status=status.HTTP_200_OK)