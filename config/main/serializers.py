from django.db.models import fields
from rest_framework import serializers
from .models import Poll, Responde


class RespondeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responde
        fields = '__all__'
        # exclude = ['update']


class PollSerializer(serializers.ModelSerializer):

    respondes = serializers.SerializerMethodField()

    class Meta:
        model = Poll
        fields = '__all__'

    def get_respondes(self, obj):
        data = obj.responde_set.all()
        result = RespondeSerializer(instance=data, many=True)
        return result.data
