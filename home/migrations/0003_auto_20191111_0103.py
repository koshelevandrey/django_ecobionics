# Generated by Django 2.2.4 on 2019-11-10 22:03

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_announce_presentation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announce',
            name='preview_image',
            field=models.ImageField(default=-1, upload_to=home.models.user_directory_path),
            preserve_default=False,
        ),
    ]
