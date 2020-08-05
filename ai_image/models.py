from django.db import models

# Create your models here.
class Document(models.Model):
    description = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='document/')
    uploaded_at = models.DateTimeField(auto_now_add=True)