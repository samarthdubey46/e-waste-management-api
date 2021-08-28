from rest_framework import serializers

from .models import *


class BlogSerializer(serializers.ModelSerializer):
    writtenBy = serializers.PrimaryKeyRelatedField(read_only=True, allow_null=True)

    class Meta:
        model = Blog
        fields = ['pk', 'title', 'image', 'writtenBy', 'writtenOn', 'description']

    def create(self, validated_data):
        user = self.context['request'].user
        return Blog.objects.create(**{**validated_data, 'writtenBy': user})
