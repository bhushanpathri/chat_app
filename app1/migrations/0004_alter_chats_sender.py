# Generated by Django 3.2.5 on 2021-08-04 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_rename_room_no_room_room_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chats',
            name='sender',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]