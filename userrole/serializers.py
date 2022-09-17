from django.contrib.auth import authenticate, get_user_model
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm
from rest_framework import serializers, exceptions
from rest_framework_simplejwt.state import token_backend
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings as simplejwt_api_settings
# Get the UserModel
UserModel = get_user_model()
# librarian=librarian


class LoginSerializer(TokenObtainSerializer):
    user = None

    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def authenticate(self, **kwargs):
        return authenticate(self.context['request'], **kwargs)

    def _validate_username_email(self, username, password):
        print("inside validate username ", username, password)
        if username and password:
            user = self.authenticate(username=username, password=password)
        else:
            msg = 'Must include both "username" and "password".'
            raise exceptions.ValidationError(msg)
        return user

    def validate(self, attrs):

        print("validate function")
        username = attrs.get('username')
        password = attrs.get('password')
        # tab_id = attrs.get('tab_id')

        user = self._validate_username_email(username, password)

        if user:
            if not user.is_active:
                msg = 'User account is disabled.'
                raise exceptions.ValidationError(msg)
        else:
            msg = 'invalid credentials'
            raise exceptions.ValidationError(msg)
        refresh = self.get_token(user)
        data = {}
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data
