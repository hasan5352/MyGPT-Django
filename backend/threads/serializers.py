from rest_framework import serializers
from .models import Thread, Message

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        exclude = ['user']

    def create(self, validated_data):
        request = self.context['request']
        return Thread.objects.create(user=request.user, **validated_data)        

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ['role']

class MessageInputSerializer(serializers.Serializer):
    message = serializers.CharField(required=True, allow_blank=False)