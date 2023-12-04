# Generated by Django 4.2.6 on 2023-11-16 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='', verbose_name='Логотип турнира')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название клуба')),
                ('points', models.IntegerField(verbose_name='Очки')),
                ('goals', models.IntegerField(verbose_name='Забито')),
                ('conceded', models.IntegerField(verbose_name='Пропущено')),
                ('info', models.TextField(verbose_name='Информация о команде')),
                ('team_logo', models.ImageField(upload_to='', verbose_name='Логотип команды')),
                ('win', models.IntegerField(verbose_name='Кол-во побед')),
                ('loss', models.IntegerField(default=0, verbose_name='Кол-во ничьих')),
                ('draw', models.IntegerField(default=0, verbose_name='Кол-во поражений')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='my_app.tournament')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('nationality', models.TextField(verbose_name='Национальность')),
                ('goals', models.IntegerField(default=0, verbose_name='Кол-во голов')),
                ('passes', models.IntegerField(default=0, verbose_name='Кол-во голевых передач')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='my_app.team')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(verbose_name='Время')),
                ('date', models.DateField(verbose_name='Дата')),
                ('goals_first_team', models.IntegerField(default='-', verbose_name='Кол-во голов первой команды')),
                ('goals_second_team', models.IntegerField(default='-', verbose_name='Кол-во голов второй команды')),
                ('first_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches1', to='my_app.team')),
                ('second_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches2', to='my_app.team')),
            ],
        ),
    ]
