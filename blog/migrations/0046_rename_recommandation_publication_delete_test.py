# Generated by Django 4.0.4 on 2022-05-15 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0045_remove_recommandation_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='recommandation',
            new_name='publication',
        ),
        migrations.DeleteModel(
            name='test',
        ),
    ]