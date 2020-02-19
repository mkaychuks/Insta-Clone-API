from django.contrib.auth.models import User

from rest_framework import serializers

from .models import UserProfile
from instaclone.models import Upload


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class UploadListSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Upload
        fields = ['picture', 'datestamp', 'timestamp', 'description', 'author']
    
    def get_author(self, obj):
        return obj.author.username



class UserProfileSerializer(serializers.ModelSerializer):
    users = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['display_picture', 'display_name', 'bio', 'date_of_birth', 'users', 'id']


class UserProfileUploads(serializers.ModelSerializer):
    uploads = UploadListSerializer()

    class Meta:
        model = UserProfile
        fields = ['id', 'uploads']