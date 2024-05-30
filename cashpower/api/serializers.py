from rest_framework import serializers
from .models import User, Request, Upload, Dispense


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
        
# class ClientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Client
#         fields = "__all__"
        

class RequestSerializer(serializers.ModelSerializer): 
    client = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    
    class Meta:
        model = Request
        fields = "__all__"
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        client = User.objects.get(pk=representation['client'])
        representation['client'] = {
            "id": client.id,
            "first_name": client.first_name,
            "last_name": client.last_name,
            "phone_number": client.phone_number,
            "id_card_number": client.id_card_number
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