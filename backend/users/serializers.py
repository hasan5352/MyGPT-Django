from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}, }
        read_only_fields = ['id']       # created_at and updated_at not needed as they are already read_only due to auto & editable=False