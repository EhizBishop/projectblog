# Generated by Django 4.0.5 on 2022-07-07 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_post_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]