# Generated by Django 3.0.4 on 2020-03-27 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listitem',
            old_name='item',
            new_name='todo_item',
        ),
        migrations.RemoveField(
            model_name='listitem',
            name='completed',
        ),
    ]
