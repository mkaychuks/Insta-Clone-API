from django.db import models
from django.contrib.auth.models import User


class Upload(models.Model):
    picture = models.ImageField(upload_to='mobile-uploads')
    description = models.TextField()
    datestamp = models.DateField(auto_now_add=True)
    timestamp = models.TimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return f'{self.author.username} posted {self.picture} by {self.timestamp} UTC-8'