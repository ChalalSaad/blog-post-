# Generated by Django 4.0.3 on 2022-04-18 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_detail',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]