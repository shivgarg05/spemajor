import logging
from rest_framework import viewsets, permissions
from .models import Blog
from .serializers import BlogSerializer

logger = logging.getLogger(__name__)


class BlogViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = BlogSerializer

    def get_queryset(self):
        logger.info('Retrieving blogs for user %s', self.request.user.username)
        # show the blogs of the requested user only
        return self.request.user.blogs.all()  # as related_name (in models) = blogs

    # saving user credentials (through owner field) in serializer
    def perform_create(self, serializer):
        logger.info('Creating new blog post for user %s', self.request.user.username)
        serializer.save(owner=self.request.user)
