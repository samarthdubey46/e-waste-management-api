from django.db import models

from User.models import User


class Complaint(models.Model):
    TICKET_STATUS = (
        ('1', "Pending"),
        ('2', "In Progress"),
        ('3', "Completed"),
    )
    PRIORITY_CHOICES = (
        ('1', "High"),
        ('2', "Moderate"),
        ('3', "Low"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    # to = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name='to_user')
    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.TextField(null=True)
    long = models.FloatField(null=True)
    lat = models.FloatField(null=True)
    category = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=20, null=True)
    seen = models.BooleanField(default=False)
    status = models.CharField(max_length=100, choices=TICKET_STATUS, default=TICKET_STATUS[0][0])
    priority = models.CharField(max_length=100, choices=PRIORITY_CHOICES, default=PRIORITY_CHOICES[2][0], null=True)
    image_1 = models.ImageField(null=True, upload_to='image/complaints/', blank=True)
    image_2 = models.ImageField(null=True, upload_to='image/complaints/', blank=True)
    image_3 = models.ImageField(null=True, upload_to='image/complaints/', blank=True)
    image_4 = models.ImageField(null=True, upload_to='image/complaints/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_image(self):
        return self.image_1

    def __str__(self):
        return self.title
# Create your models here.
