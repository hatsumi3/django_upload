from django.db import models

class Document(models.Model):
    """写真とその説明を管理するモデル

    Attributes:
        description(str): 説明
        photo(str): 画像パス
        uploaded_at(str): 日付
    """
    description = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='document/')
    uploaded_at = models.DateTimeField(auto_now_add=True)