from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from .pagination import CustomPagination
from .permissions import IsAdminUserOrReadOnly
from .serializers import *


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = (filters.SearchFilter,filters.OrderingFilter)
    search_fields = ['title']