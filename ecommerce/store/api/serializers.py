from rest_framework import serializers
from .models import Music

class MusicSerializer(serializers.Serializer):
    class Meta:
        model = Music
        fields = '__all__'
         