from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response
from .permisions import PermissionCuston
from .models import User
from .serializer import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserViels(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, 201)

class LoginJWTView(TokenObtainPairView):
    pass

class UserDetailViels(APIView):
    permission_classes = [IsAuthenticated, PermissionCuston]
    authentication_classes = [JWTAuthentication]

    def get(self, request: Request, movie_id: int) -> Response:
        user = get_object_or_404(User, id=movie_id)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=200)
    
    def patch(self, request: Request, movie_id: int) -> Response:
        user = get_object_or_404(User, id=movie_id)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)