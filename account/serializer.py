from rest_framework import serializers
from .models import  Account

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = Account
        fields = ['email','username','password','confirm_password']
        extra_kwargs = {
            'password':{'write_only':True}
        }
    def save(self):
        account = Account(
                    email=self.validated_data['email']
                    username = self.validate_data['username']
        ) 
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password'] 

        if password != confirm_password:
            return serializers.ValidationError({'password':'Passwords don`t match.'})

        account.set_password(password)
        account.save()    