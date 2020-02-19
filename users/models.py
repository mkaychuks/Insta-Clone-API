from django.db import models
from django.contrib.auth.models import User

from instaclone.models import Upload


class UserProfile(models.Model):
    display_picture = models.ImageField(upload_to='profile_pictures', default='logo.jpg')
    display_name = models.CharField(max_length=100)
    bio = models.TextField()
    date_of_birth = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    uploads = models.ForeignKey(Upload, on_delete=models.CASCADE, related_name='uploads')

    class Meta:
        verbose_name_plural = 'Users\' Profile'

    def __str__(self):
        return self.user.username
