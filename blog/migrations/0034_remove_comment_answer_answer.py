# Generated by Django 4.0.4 on 2022-05-11 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_comment_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='answer',
        ),
        migrations.CreateModel(
            name='answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='blog.comment')),
            ],
        ),
    ]
