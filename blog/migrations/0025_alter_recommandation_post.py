# Generated by Django 4.0.4 on 2022-05-07 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_recommandation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommandation',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recommandations', to='blog.post'),
        ),
    ]
