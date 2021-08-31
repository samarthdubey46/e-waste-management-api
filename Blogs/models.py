import math

from django.db import models

from User.models import User


class Blog(models.Model):
    title = models.CharField(max_length=300, unique=True)
    # TODO Add default Image
    image = models.ImageField(null=True, upload_to='image/blogs/')
    category = models.CharField(max_length=100, default='Awareness')
    description = models.TextField()
    writtenBy = models.ForeignKey(User, on_delete=models.CASCADE)
    writtenOn = models.DateTimeField(auto_now_add=True)

    def getTime(self):
        description_count = len(self.description.split())
        count = description_count / 100
        unit = 'min'
        time = math.ceil(count)
        if count < 1:
            unit = 'secs'
            time = math.ceil(count * 60)
        if count >= 60:
            unit = 'hrs'
            time = math.ceil(count / 60)
        return f"{time} {unit} read"

    def __str__(self):
        return self.title
