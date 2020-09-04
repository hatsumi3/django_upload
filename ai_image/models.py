from django.db import models
from django.conf import settings
from PIL import Image


class Document(models.Model):
    """写真とその説明を管理するモデル

    Attributes:
        description(str): 説明
        photo(str): 画像パス
        uploaded_at(str): 日付
    """
    description = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='document/')
    bw_photo = models.ImageField(upload_to='document_bw/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def make_bw_image(self):
        img = Image.open(self.photo)
        gray_img = img.convert('L')
        bw_image_path = f'{settings.MEDIA_ROOT}/{Document.bw_photo.field.upload_to}{self.photo}'
        gray_img.save(bw_image_path)
        self.bw_photo = bw_image_path