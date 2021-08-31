from rest_framework import serializers

from User.serializers import UserSerializer
from .models import *


class BlogRegisterSerializer(serializers.ModelSerializer):
    writtenBy = serializers.PrimaryKeyRelatedField(read_only=True, allow_null=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'image', 'writtenBy', 'writtenOn', 'description']

    def create(self, validated_data):
        user = self.context['request'].user
        return Blog.objects.create(**{**validated_data, 'writtenBy': user})


class BlogSingleSerializer(serializers.ModelSerializer):
    writtenBy = UserSerializer(many=False)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'image', 'writtenBy', 'writtenOn', 'description']


class BlogSerializer(serializers.ModelSerializer):
    readTime = serializers.CharField(source='getTime')

    class Meta:
        model = Blog
        fields = ['id', 'title', 'image', 'writtenOn', 'readTime']
