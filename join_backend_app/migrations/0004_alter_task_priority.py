# Generated by Django 5.1.4 on 2025-01-07 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_backend_app', '0003_remove_task_users_alter_contact_user_task_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.IntegerField(default='2'),
        ),
    ]