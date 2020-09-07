from django.contrib import admin
from django.utils import timezone
from .models import Document
# Register your models here.

from django.db.models.signals import pre_save
from django.dispatch import receiver

class DocumentAdmin(admin.ModelAdmin):
    """Django 管理画面で表示する内容を設定するクラス
    表示する項目、読み取りのみ、表示順序、検索項目の指定を実施。

    Args:
        admin ([type]): [description]
    """
    list_display = ('id', 'photo', 'sample_number','uploaded_at', 'description')
    readonly_fields = ('uploaded_at',)
    ordering = ('-uploaded_at',)
    search_fields = ('description',)

@receiver(pre_save, sender=Document)
def my_handler(sender, instance, **kwargs):
    instance.uploaded_at = timezone.now()

admin.site.register(Document, DocumentAdmin)