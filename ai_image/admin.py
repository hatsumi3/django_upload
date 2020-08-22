from django.contrib import admin
from .models import Document
# Register your models here.

class DocumentAdmin(admin.ModelAdmin):
    """Django 管理画面で表示する内容を設定するクラス
    表示する項目、読み取りのみ、表示順序、検索項目の指定を実施。

    Args:
        admin ([type]): [description]
    """
    list_display = ('id', 'photo', 'uploaded_at', 'description')
    read_only_fields = ('uploaded_at',)
    ordering = ('-uploaded_at',)
    search_fields = ('description',)

admin.site.register(Document, DocumentAdmin)