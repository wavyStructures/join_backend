# Generated by Django 5.1.4 on 2024-12-27 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_backend_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
        migrations.AddField(
            model_name='task',
            name='users',
            field=models.ManyToManyField(to='join_backend_app.user'),
        ),
    ]