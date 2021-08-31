from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from .permissions import IsAdminUserOrReadOnly
from .serializers import *


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['title']

    def __init__(self, *args, **kwargs):
        super(BlogViewSet, self).__init__(*args, **kwargs)
        self.serializers = {
            'list': BlogSerializer,
            'retrieve': BlogSingleSerializer,
        }

    def get_serializer_class(self, *args, **kwargs):
        """Instantiate the list of serializers per action from class attribute (must be defined)."""
        kwargs['partial'] = True
        try:
            return self.serializers[self.action] if self.action in self.serializers else BlogRegisterSerializer
        except (KeyError, AttributeError):
            return super(BlogViewSet, self).get_serializer_class()

