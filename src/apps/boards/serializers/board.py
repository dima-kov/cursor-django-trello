from rest_framework import serializers

from apps.boards.models import Board, Col, Task
from apps.boards.serializers.comment import CommentSerializer
from apps.users.models import TrelloUser
from apps.users.serializers.users import TrelloUserShortSerializer


class TaskSerializer(serializers.ModelSerializer):
    created_by = TrelloUserShortSerializer()
    col = serializers.IntegerField(source='col_id')
    comments = CommentSerializer(many=True)

    class Meta:
        model = Task
        fields = ('id', 'name', 'status', 'description', 'created_by', 'col', 'comments')


class ColumnSerializer(serializers.ModelSerializer):
    board = serializers.PrimaryKeyRelatedField(queryset=Board.objects.all(), write_only=True)
    tasks = TaskSerializer(many=True)

    class Meta:
        model = Col
        fields = ('name', 'position', 'board', 'tasks')


class BoardSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=TrelloUser.objects.all(), write_only=True)
    columns = ColumnSerializer(many=True, source='cols', read_only=True)

    class Meta:
        model = Board
        fields = ('id', 'created_at', 'updated_at', 'name', 'owner', 'columns')
