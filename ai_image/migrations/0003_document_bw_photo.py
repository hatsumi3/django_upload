# Generated by Django 3.1 on 2020-09-04 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai_image', '0002_auto_20200805_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='bw_photo',
            field=models.ImageField(blank=True, null=True, upload_to='document_bw/'),
        ),
    ]
