from django.db import models

from User.models import User


class Complaint(models.Model):
    TICKET_STATUS = (
        ('1', "Pending"),
        ('2', "OnGoing"),
        ('3', "Completed"),
    )
    PRIORITY_CHOICES = (
        ('1', "High"),
        ('2', "Moderate"),
        ('3', "Low"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    to = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name='to_user')
    title = models.CharField(max_length=255)
    description = models.TextField()
    seen = models.BooleanField(default=False)
    status = models.CharField(max_length=100, choices=TICKET_STATUS, default=TICKET_STATUS[0][0])
    priority = models.CharField(max_length=100, choices=PRIORITY_CHOICES, default=PRIORITY_CHOICES[2][0], null=True)
    image_1 = models.ImageField(null=True, upload_to='image/complaints/')
    image_2 = models.ImageField(null=True, upload_to='image/complaints/')
    image_3 = models.ImageField(null=True, upload_to='image/complaints/')
    image_4 = models.ImageField(null=True, upload_to='image/complaints/')
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
