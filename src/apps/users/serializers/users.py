from rest_framework import serializers

from apps.users.models import TrelloUser


class TrelloUserShortSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fullname = serializers.SerializerMethodField()
    avatar = serializers.ImageField(read_only=True)

    def get_fullname(self, obj: TrelloUser) -> str:
        """
        :param obj:
        :return:
        """
        return obj.get_full_name()
