from rest_framework import serializers
from users.models import User
from rest_framework.validators import UniqueValidator

class SignupSerializer(serializers.Serializer):
	email = serializers.EmailField(
		required=True,  
		validators=[UniqueValidator(queryset=User.objects.all())] 
	)
	password = serializers.CharField(required=True, min_length=1)

	def create(self, validated_data):
		return User.objects.create_user(
			email=validated_data['email'],
			password=validated_data['password']
		)
	

class LoginSerializer(serializers.Serializer):
	email = serializers.EmailField(required=True)
	password = serializers.CharField(required=True, min_length=1)

	def validate(self, data):
		email = data.get("email")
		password = data.get("password")

		try:
			user = User.objects.get(email=email)
		except:
			raise serializers.ValidationError("User does not exist. Please signup.", code=400)

		if not user.check_password(password):
			raise serializers.ValidationError("Invalid Credentials", code=400)
		
		data['user'] = user
		return data
	
