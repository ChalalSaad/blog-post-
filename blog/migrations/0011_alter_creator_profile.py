# Generated by Django 4.0.4 on 2022-05-01 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creator',
            name='profile',
            field=models.CharField(max_length=5000000000),
        ),
    ]
