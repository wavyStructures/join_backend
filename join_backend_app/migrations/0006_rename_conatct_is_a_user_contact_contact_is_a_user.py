# Generated by Django 5.1.4 on 2025-01-21 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('join_backend_app', '0005_remove_contact_users_contact_conatct_is_a_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='conatct_is_a_user',
            new_name='contact_is_a_user',
        ),
    ]
