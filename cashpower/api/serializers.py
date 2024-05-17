from rest_framework import serializers
from .models import User, Client, Request, Upload, Dispense


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
        
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
        

class RequestSerializer(serializers.ModelSerializer): 
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    
    class Meta:
        model = Request
        fields = "__all__"
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        client = User.objects.get(pk=representation['client'])
        representation['client'] = {
            "id": client.id,
            "first_name": client.first_name,
            "last_name": client.last_name
        }
        return representation
    
        
class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = "__all__"
        
        
class DispenseSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Dispense
        fields = "__all__"