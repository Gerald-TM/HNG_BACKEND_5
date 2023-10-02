from django.db import models

# Create your models here.
class Video(models.Model):
    session_id = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    chunk_number = models.IntegerField()
    data = models.BinaryField()