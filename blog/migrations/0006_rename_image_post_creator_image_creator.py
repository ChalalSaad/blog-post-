# Generated by Django 4.0.3 on 2022-04-22 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_creator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='creator',
            old_name='image_post',
            new_name='image_creator',
        ),
    ]
