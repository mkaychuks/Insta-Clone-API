from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Upload
from users.serializers import UserSerializer



class UploadSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Upload
        fields = '__all__'


class UploadListSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Upload
        fields = ['picture', 'datestamp', 'timestamp', 'description', 'author']
        ref_name = 'Uploads'
    
    def get_author(self, obj):
        return obj.author.username