# Generated by Django 3.2.3 on 2021-05-30 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='cleated_at',
            new_name='created_at',
        ),
    ]
