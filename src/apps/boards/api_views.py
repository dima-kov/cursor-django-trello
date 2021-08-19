from django.db.models import Prefetch, Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.boards.models import Board, Task
from apps.boards.permissions import BoardReadOnlyOrIsOwnerOnly
from apps.boards.serializers.board import BoardSerializer


class BoardListCreateView(generics.ListCreateAPIView):
    serializer_class = BoardSerializer
    permission_classes = (IsAuthenticated, BoardReadOnlyOrIsOwnerOnly)
    # CACHE_TTL = 60

    def get_queryset(self):
        queryset = Board.objects.all()

        col_tasks_pref = Prefetch(
            'cols__tasks', Task.objects.select_related('created_by').prefetch_related('comments')
        )
        collection_lookups = Q(users__in=(self.request.user,)) | Q(owner=self.request.user)
        return queryset.filter(collection_lookups).prefetch_related(col_tasks_pref)


class BoardDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, BoardReadOnlyOrIsOwnerOnly)

    def get_queryset(self):
        # TODO move logic to Board Manager
        queryset = Board.objects.all()

        col_tasks_pref = Prefetch(
            'cols__tasks', Task.objects.select_related('created_by').prefetch_related('comments')
        )
        collection_lookups = Q(users__in=(self.request.user,)) | Q(owner=self.request.user)
        return queryset.filter(collection_lookups).prefetch_related(col_tasks_pref)
