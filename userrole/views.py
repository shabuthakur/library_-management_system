from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework.permissions import AllowAny
from userrole.serializers import *
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt

from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

# Create your views here.


class LoginView(TokenViewBase):
    permission_classes = [AllowAny, ]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(
                data=request.data, context={'request': request})
            try:
                serializer.is_valid(raise_exception=True)
            except TokenError as e:
                raise InvalidToken(e.args[0])
            return Response({'status': 'STATUS', 'data': serializer.validated_data}, status=200)
        except Exception as e:
            return Response({'status': 'ERROR', 'message': str(e)}, status=400)
