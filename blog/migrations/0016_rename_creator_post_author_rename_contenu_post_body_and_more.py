# Generated by Django 4.0.4 on 2022-05-02 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='creator',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='contenu',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='titre',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='typeContenu',
            new_name='title',
        ),
    ]
