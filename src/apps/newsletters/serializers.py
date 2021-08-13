from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.newsletters.models import Subscriber


class SubscriberSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    reversed_email = serializers.SerializerMethodField(method_name='reversed_email_fields')

    def reversed_email_fields(self, obj):
        return obj.email[::-1]

    def validate_email(self, value: str) -> str:
        """Validate subscriber email
        :param value: email
        :return:
        """
        if Subscriber.objects.filter(email=value).exists():
            raise ValidationError("You are already subscribed.")
        return value

    def create(self, validated_data):
        return Subscriber.objects.create(email=validated_data.get('email'))

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email')
        instance.save()
        return instance


class SubscriberModelSerializer(serializers.ModelSerializer):
    reversed_email = serializers.SerializerMethodField(method_name='reversed_email_fields')

    class Meta:
        model = Subscriber
        fields = ['email', 'reversed_email']

    def reversed_email_fields(self, obj):
        return obj.email[::-1]
