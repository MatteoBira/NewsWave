# Generated by Django 4.2.4 on 2023-08-24 15:52

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_profile_profile_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('cover_img', models.ImageField(upload_to='post_images')),
                ('title', models.TextField(max_length=100)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]