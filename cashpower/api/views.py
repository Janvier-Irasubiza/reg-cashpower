from django.http import Http404
from django.shortcuts import render
from .models import User, Client, Request, Upload, Dispense
from .serializers import UserSerializer, ClientSerializer, RequestSerializer, UploadSerializer, DispenseSerializer
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist


# Admin login
# -----------
@api_view(['POST'])
def admin_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response({
            'detail': 'Username and password are required.'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    user = authenticate(username=username, password=password)
    
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(instance=user)
        
        user_info = {
            "id": serializer.data['id'],
            "username": serializer.data['username'],
            "email": serializer.data['email'],
        }
        
        return Response({
            "success": "Authenticated successfully",
            "token": token.key, 
            "user": user_info,
            "dashboard_url": "/admin/dashboard"
        }, status=status.HTTP_200_OK)
    
    return Response({
        "detail": "Invalid credentials."
    }, status=status.HTTP_401_UNAUTHORIZED)



# Client login
# ------------
@api_view(['POST'])
def client_login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    if not email or not password:
        return Response({
            'detail': 'Email and password are required.'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    user = authenticate(email=email, password=password)
    
    if user is None:
        try:
            user = Client.objects.get(email=email)
            user = authenticate(email=user.email, password=password)
        except Client.DoesNotExist:
            return Response({
                'detail': 'Invalid credentials.'
            }, status=status.HTTP_401_UNAUTHORIZED)
    
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        serializer = ClientSerializer(instance=user)
        
        user_info = {
            "id": serializer.data['id'],
            "username": serializer.data['username'],
            "email": serializer.data['email'],
        }
        
        return Response({
            "success": "Authenticated successfully",
            "token": token.key, 
            "user": user_info,
            "dashboard_url": "/admin/dashboard"
        }, status=status.HTTP_200_OK)
    
    return Response({
        "detail": "Invalid credentials."
    }, status=status.HTTP_401_UNAUTHORIZED)


# Logout
# ------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    try:
        request.user.auth_token.delete()
    except (AttributeError, ObjectDoesNotExist):
        return Response({
            "detail": "User does not have an active session."
        }, status=status.HTTP_400_BAD_REQUEST)
    
    request.session.flush()    
    logout(request)
    
    return Response({
        "success": "Logged out successfully",
    }, status=status.HTTP_200_OK)
    

# Get and post all users
# -------------
class GetAllUsers(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    

# Get specific user
# -----------------
class GetUser(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    lookup_field = 'id'
    
    def get_queryset(self):
        user_id = self.kwargs.get('id')
        if user_id is not None:
            try:
                return User.objects.filter(pk=user_id)
            except User.DoesNotExist:
                raise Http404("User does not exist")
        else:
            return User.objects.none()
        

# Get and post clients
# --------------------
class ClientsView(generics.ListCreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


# Get, update, and delete client
# ------------------------------
class ClientView(generics.RetrieveUpdateAPIView):
    serializer_class = ClientSerializer
    
    def get_queryset(self):
        client = self.kwargs.get('client')
        
        if client is not None:
            try:
                return Client.objects.filter(pk=client)
            except Client.DoesNotExist:
                return Http404('Client does not exists')
        else:
            return Client.objects.none()
        
    
# Get and post Requests
# ---------------------
class RequestsView(generics.ListCreateAPIView):
    serializer_class = RequestSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Request.objects.all()
        return queryset
    
    
# Get, update, and delete single Request
# ------------------
class RequestView(generics.RetrieveAPIView):
    serializer_class = RequestSerializer

    def get_queryset(self, *args, **kwargs):
        req = self.kwargs.get('req')
        
        if req is not None:
            queryset = Request.objects.get(pk=req)
        else:
            queryset = Request.objects.none
        
        return queryset
    

# Get and post uploads
# --------------------
class UploadsView(generics.ListCreateAPIView):
    serializer_class = UploadSerializer
    
    def get_queryset(self):
        queryset = Upload.objects.all()
        return queryset
    

# Get uploads for a request
# -------------------------
class UploadsByRequestView(generics.ListCreateAPIView):
    serializer_class = UploadSerializer
    
    def get_queryset(self):
        req = self.kwargs.get('req')
        queryset = Upload.objects.filter(request=req)
        
        return queryset

# Get and post dispenses
# ----------------------
class DispensesView(generics.ListCreateAPIView):
    serializer_class = DispenseSerializer
    queryset = Dispense.objects.all()
    

# Get, update, and delete single dispense
# ----------------------------------------
class DispenseView(generics.RetrieveUpdateAPIView):
    serializer_class = DispenseSerializer
    
    def get_queryset(self):
        id = self.kwargs.get('id')
        
        if id is not None:
            queryset = Dispense.objects.get(pk=id)
        
        return queryset