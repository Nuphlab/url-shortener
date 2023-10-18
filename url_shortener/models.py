from django.db import models

class ShortenedURL(models.Model):
    original_url = models.URLField(max_length=200)
    short_url = models.CharField(max_length=10, unique=True)
