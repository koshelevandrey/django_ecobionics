# Generated by Django 2.2.4 on 2019-10-13 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announce',
            name='presentation',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
