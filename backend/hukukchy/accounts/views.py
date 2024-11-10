from rest_framework.response import Response
from rest_framework import generics, permissions, status
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer ,ChangePasswordSerializer, ResetPasswordEmailSerializer
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer 
from knox.views import LoginView as KnoxLoginView


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.first_name = request.data.get('first_name')
        user.last_name = request.data.get('last_name')
        user.save()
        token = AuthToken.objects.create(user=user)  
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user=user)[1]  
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        # Serialize the request data
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        login(request, user)
        response = super(LoginAPI, self).post(request, format=None)
        
        user_data = {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name
        }
        
        response.data['user_data']=user_data
        
        return response
    
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model=User
    # permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'user': UserSerializer(self.object).data,
                'token': AuthToken.objects.create(self.object)[1]
            }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

