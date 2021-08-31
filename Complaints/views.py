import requests
from PIL import Image
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Complaint
from .serializers import ComplaintSerializer, ComplaintListSerializer


class ComplaintsView(ModelViewSet):
    serializer_class = ComplaintSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self, *args, **kwargs):
        """Instantiate the list of serializers per action from class attribute (must be defined)."""
        kwargs['partial'] = True
        try:
            if self.action == 'list':
                return ComplaintListSerializer
            return ComplaintSerializer
        except (KeyError, AttributeError):
            return super(ComplaintsView, self).get_serializer_class()

    def get_queryset(self):
        """
        Filters the Complaints based on authenticated token
        """
        user = self.request.user
        if user.is_admin:
            return Complaint.objects.all()
        return Complaint.objects.filter(user=user)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    print(request.FILES)
    return Response(request.data)


@api_view(['GET'])
def counter(request):
    queryset = Complaint.objects.filter()
    pending = queryset.filter(status="1")
    in_progress = queryset.filter(status="2")
    completed = queryset.filter(status="3")

    return Response({'pending': len(pending), 'completed': len(completed), 'progress': len(in_progress)})
# Create your views here.
