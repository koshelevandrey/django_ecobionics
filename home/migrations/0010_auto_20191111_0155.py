# Generated by Django 2.2.4 on 2019-11-10 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20191111_0151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announce',
            old_name='word_file',
            new_name='document',
        ),
    ]