from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from backend.utils.responses import send_json
from backend.utils.auth import generate_token

from .serializers import SignupSerializer, LoginSerializer


class SignupApi(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.save()
        token = generate_token(user)

        return send_json(message="Signup successful", body={"token": token})
        

class LoginApi(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        token = generate_token(user)
        
        return send_json(message="Login successful", body={"token": token})

class VerifyJwtApi(APIView):
    def post(self, request):
        print(request.data['email'])
        return send_json(message="Verification successful")
