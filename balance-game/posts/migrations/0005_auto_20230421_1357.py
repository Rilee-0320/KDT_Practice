# Generated by Django 3.2.18 on 2023-04-21 04:57

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20230421_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image1',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image2',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]