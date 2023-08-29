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
    description = models.TextField(default="this is a description", blank="False")
    date = models.DateTimeField(default=datetime.now)
    min_read = models.IntegerField(default=1)  # Default value for min_read

    def formatted_date(self):
        return self.date.strftime("%-m/%-d/%y")

    def minute_of_reading(self, content: str) -> int:
        words = content.split()
        words_count = len(words)
        return int(words_count / 200)

    def save(self, *args, **kwargs):
        # Calculate min_read using the minute_of_reading method
        self.min_read = self.minute_of_reading(self.content) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user
