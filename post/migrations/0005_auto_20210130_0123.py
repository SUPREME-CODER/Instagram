# Generated by Django 3.0.3 on 2021-01-29 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_like', to='post.Post'),
        ),
    ]
