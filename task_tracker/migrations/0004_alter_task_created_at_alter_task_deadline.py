# Generated by Django 5.1.4 on 2024-12-26 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_tracker', '0003_task_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(),
        ),
    ]
