# Generated by Django 5.1.4 on 2024-12-26 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['is_done', '-created_at']},
        ),
    ]