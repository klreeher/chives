# works/serializers.py

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Work

class WorkSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Work
        fields = ('id', 'title', 'owner',)
