# Generated by Django 4.0.4 on 2022-05-12 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0038_remove_answer_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='answer',
        ),
        migrations.AddField(
            model_name='comment',
            name='response',
            field=models.TextField(default='answer'),
        ),
    ]
