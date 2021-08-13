from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.newsletters.models import Subscriber
from apps.newsletters.serializers import SubscriberModelSerializer, SubscriberSerializer


class SubscriberCreateList(generics.ListCreateAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberModelSerializer


class SubscriberView(APIView):

    def get(self, request):
        # not paginated
        objects = Subscriber.objects.all()
        serializer = SubscriberModelSerializer(instance=objects)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SubscriberModelSerializer(data=self.request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
