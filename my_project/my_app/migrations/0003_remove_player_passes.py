# Generated by Django 4.2.6 on 2023-11-16 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_alter_team_team_logo_alter_tournament_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='passes',
        ),
    ]
