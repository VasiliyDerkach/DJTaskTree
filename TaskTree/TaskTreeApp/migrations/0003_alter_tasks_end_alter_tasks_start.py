# Generated by Django 4.2.16 on 2024-11-10 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskTreeApp', '0002_alter_tasks_end_alter_tasks_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='end',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='start',
            field=models.DateField(null=True),
        ),
    ]
