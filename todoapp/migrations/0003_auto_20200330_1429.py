# Generated by Django 2.2.11 on 2020-03-30 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_auto_20200327_1753'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listitem',
            old_name='todo_item',
            new_name='item',
        ),
    ]
