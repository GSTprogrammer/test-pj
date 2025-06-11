from rest_framework import serializers
from .models import CustomUser,Project,Proposal
from django.contrib.auth.password_validation import validate_password

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'user_type']

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            user_type=validated_data['user_type']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'created_at']
        read_only_fields = ['id', 'created_at']

class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ['id', 'project', 'message', 'proposed_price', 'status', 'created_at']
        read_only_fields = ['id', 'status', 'created_at']