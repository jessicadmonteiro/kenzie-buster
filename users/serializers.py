from rest_framework import serializers
from users.models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150, validators=[UniqueValidator(queryset=User.objects.all(), message=("username already taken."))])
    email = serializers.EmailField(max_length=127, validators=[UniqueValidator(queryset=User.objects.all(), message=("email already registered."))])
    birthdate = serializers.DateField(allow_null=True, default=None)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=127, write_only=True)
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(default=False, read_only=True)

    def create(self, validated_data):

        if validated_data["is_employee"]:
            validated_data["is_superuser"] = True

        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.set_password(instance.password)
        instance.save()

        return instance
