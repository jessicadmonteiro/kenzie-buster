from rest_framework.views import APIView, Response
from users.serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data, 201)


class LoginView(TokenObtainPairView):
    ...
