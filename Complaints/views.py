from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Complaint
from .serializers import ComplaintSerializer


class ComplaintsView(ModelViewSet):
    serializer_class = ComplaintSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Filters the Complaints based on authenticated token
        """
        user = self.request.user
        if user.is_admin:
            return Complaint.objects.all()
        return Complaint.objects.filter(user=user)

# Create your views here.
