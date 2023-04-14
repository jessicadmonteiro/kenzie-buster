from rest_framework.views import APIView, Response
from users.serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from .permissions import PermissionsIdUser
from django.shortcuts import get_object_or_404
from .models import User


class LoginView(TokenObtainPairView):
    ...


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data, 201)


class UserParamView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [PermissionsIdUser | IsAdminUser]

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, user)

        serializer = UserSerializer(user)

        return Response(serializer.data, 200)

    def patch(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, user)

        serializer = UserSerializer(instance=user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, 200)
