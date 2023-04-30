# view for registering users
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import UserData
from .serializers import UserSerializer
from .swagger.authentification_swagger import logout_response, logout_schema, response_login, response_refresh_token, \
    register_response
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


class LoginTokenObtainPairView(TokenObtainPairView):
    @swagger_auto_schema(
        responses=response_login,
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class LoginRefreshTokenView(TokenRefreshView):
    @swagger_auto_schema(
        responses=response_refresh_token
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class RegisterView(generics.ListCreateAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['post']
    @swagger_auto_schema(
        responses=register_response,
    )
    def post(self, request):
        print("im posting new user")
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LogoutUserView(APIView):
    #permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        responses=logout_response,
        request_body=logout_schema,
    )
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({
                    "detail": "Successfully logged out"
                }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
