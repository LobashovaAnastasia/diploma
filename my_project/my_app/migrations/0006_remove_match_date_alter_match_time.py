# Generated by Django 4.2.6 on 2023-11-23 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_alter_player_nationality'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='date',
        ),
        migrations.AlterField(
            model_name='match',
            name='time',
            field=models.DateTimeField(verbose_name='Время'),
        ),
    ]