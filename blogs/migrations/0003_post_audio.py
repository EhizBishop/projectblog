# Generated by Django 4.0.5 on 2022-07-06 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_post_date_posted_alter_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='music'),
        ),
    ]
