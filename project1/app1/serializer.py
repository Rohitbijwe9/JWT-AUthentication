from django.contrib.auth import get_user_model
from rest_framework import serializers




User=get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=('id','username','password','email') #this field predefine in user model
    
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
    




