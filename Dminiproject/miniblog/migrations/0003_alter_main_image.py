# Generated by Django 4.2 on 2023-05-01 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniblog', '0002_main_image_main_updatedate_alter_main_uploaddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='miniblog/image'),
        ),
    ]
