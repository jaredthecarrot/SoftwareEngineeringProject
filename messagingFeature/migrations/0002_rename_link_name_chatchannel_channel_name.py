# Generated by Django 5.1.1 on 2024-10-27 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messagingFeature', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatchannel',
            old_name='link_name',
            new_name='channel_name',
        ),
    ]