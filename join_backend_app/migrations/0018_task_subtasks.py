# Generated by Django 5.1.4 on 2025-02-20 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_backend_app', '0017_contact_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='subtasks',
            field=models.ManyToManyField(blank=True, to='join_backend_app.task'),
        ),
    ]
