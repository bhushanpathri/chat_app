# Generated by Django 3.2.5 on 2021-07-31 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_room_code_room_room_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='room_no',
            new_name='room_name',
        ),
    ]
