# Generated by Django 4.0.4 on 2022-05-13 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0041_commentfinal_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='response',
            field=models.TextField(default='Wait ....'),
        ),
    ]
