from django.db import models

from User.models import User


class Blog(models.Model):
    title = models.CharField(max_length=300, unique=True)
    # TODO Add default Image
    image = models.ImageField(null=True,upload_to='image/blogs/')
    description = models.TextField()
    writtenBy = models.ForeignKey(User, on_delete=models.CASCADE)
    writtenOn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

