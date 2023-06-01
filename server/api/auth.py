from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from app.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


class ViewRegister(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    http_method_names = [
        "post",
    ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = User.objects.get(username=request.data["username"])
        token = Token.objects.get(user=user)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"token": token.key}, status=status.HTTP_201_CREATED, headers=headers
        )


