# Generated by Django 4.0.5 on 2022-07-07 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_like_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='video'),
        ),
    ]
