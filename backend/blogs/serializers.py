import logging
from rest_framework import serializers
from .models import Blog

logger = logging.getLogger(__name__)

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'

    def create(self, validated_data):
        logger.info('Creating new blog post with title %s', validated_data.get('title'))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        logger.info('Updating blog post with title %s', validated_data.get('title'))
        return super().update(instance, validated_data)