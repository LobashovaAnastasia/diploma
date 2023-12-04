# Generated by Django 4.2.6 on 2023-12-01 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='coefficient_loss',
            field=models.FloatField(default=0, verbose_name='Коэффициент на ничью'),
        ),
        migrations.AddField(
            model_name='match',
            name='coefficient_win_first',
            field=models.FloatField(default=0, verbose_name='Коэффициент на победу первой команды'),
        ),
        migrations.AddField(
            model_name='match',
            name='coefficient_win_second',
            field=models.FloatField(default=0, verbose_name='Коэффициент на победу второй команды'),
        ),
        migrations.AlterField(
            model_name='match',
            name='goals_first_team',
            field=models.IntegerField(blank=True, null=True, verbose_name='Кол-во голов первой команды'),
        ),
        migrations.AlterField(
            model_name='match',
            name='goals_second_team',
            field=models.IntegerField(blank=True, null=True, verbose_name='Кол-во голов второй команды'),
        ),
    ]
