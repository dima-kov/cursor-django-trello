from rest_framework.permissions import BasePermission, SAFE_METHODS

from apps.boards.models import Board


class BoardReadOnlyOrIsOwnerOnly(BasePermission):
    # def has_permission(self, request, view):
    #     return Board.objects.filter(users__in=(request.user,))

    def has_object_permission(self, request, view, obj: Board) -> bool:
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.owner
