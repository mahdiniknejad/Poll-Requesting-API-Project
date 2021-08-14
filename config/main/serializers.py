from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Poll, Responde


class RespondeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responde
        exclude = ['update']


class PollSerializer(serializers.ModelSerializer):

    responds = RespondeSerializer()

    class Meta:
        model = Poll
        fields = '__all__'
