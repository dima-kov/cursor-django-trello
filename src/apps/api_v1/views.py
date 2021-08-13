from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


@api_view(http_method_names=['GET'])
def check(request):
    return Response(data={"status": 'OK'}, status=status.HTTP_200_OK)


class HealthcheckView(APIView):
    def get(self, request):
        return Response(data={"status": 'OK'}, status=status.HTTP_200_OK)
