from django.db import models

class Document(models.Model):
    """写真とその説明を管理するモデル

    Args:
        models ([type]): 写真とその説明を管理するモデル
    """
    description = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='document/')
    uploaded_at = models.DateTimeField(auto_now_add=True)