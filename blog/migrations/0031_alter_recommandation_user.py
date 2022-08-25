# Generated by Django 4.0.4 on 2022-05-10 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0030_recommandation_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommandation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommandations', to=settings.AUTH_USER_MODEL),
        ),
    ]