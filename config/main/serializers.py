from django.db.models import fields
from rest_framework import serializers
from .models import Poll, Responde


class RespondeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responde
        fields = '__all__'
        extra_kwargs = {
            'poll': {
                'read_only': True
            }
        }


class PollSerializer(serializers.ModelSerializer):

    get_respondes = serializers.SerializerMethodField(read_only=True)

    post_respondes = serializers.ListField(
        child=serializers.JSONField(), write_only=True)

    class Meta:
        model = Poll
        fields = '__all__'

    def get_get_respondes(self, obj):
        data = obj.responde_set.all()
        result = RespondeSerializer(instance=data, many=True)
        return result.data

    def create(self, validated_data):
        poll = Poll.objects.create(
            title=validated_data.get('title'),
            description=validated_data.get('description'),
            deprecate=validated_data.get('deprecate'),
            user=validated_data.get('user'),
        )

        for responde in validated_data.get('post_respondes'):
            Responde.objects.create(
                poll=poll, title=validated_data.get('title'))
        return poll
