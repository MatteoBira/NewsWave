from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profile_img = models.ImageField(
        upload_to="profile_images", default="blank-profile-picture.png"
    )
    partnership = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    cover_img = models.ImageField(upload_to="post_images")
    title = models.TextField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user
