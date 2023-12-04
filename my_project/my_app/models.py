from django.db import models


class Tournament(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField("Логотип турнира", upload_to='images/')

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField('Название клуба', max_length=40)
    points = models.IntegerField('Очки')
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='teams')
    goals = models.IntegerField("Забито")
    conceded = models.IntegerField("Пропущено")
    info = models.TextField('Информация о команде')
    team_logo = models.ImageField("Логотип команды", upload_to='images/')
    win = models.IntegerField("Кол-во побед")
    loss = models.IntegerField("Кол-во ничьих", default=0)
    draw = models.IntegerField("Кол-во поражений", default=0)

    def __str__(self):
        return self.name


class Player(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField("Фамилия", max_length=20)
    age = models.IntegerField("Возраст")
    nationality = models.CharField("Национальность", max_length=20, default='Беларусь')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    goals = models.IntegerField("Кол-во голов", default=0)

    def __str__(self):
        return self.last_name


class News(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    text = models.TextField('Текст новости')
    date = models.DateField('Дата публикации')
    photo = models.ImageField('Фото публикации', upload_to='images/')
    category = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='news')

    def __str__(self):
        return f"{self.title}"


class Match(models.Model):
    first_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches1')
    second_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches2')
    time = models.DateTimeField("Время")
    goals_first_team = models.IntegerField("Кол-во голов первой команды", blank=True, null=True)
    goals_second_team = models.IntegerField("Кол-во голов второй команды", blank=True, null=True)
    coefficient_win_first = models.FloatField("Коэффициент на победу первой команды", default=0)
    coefficient_win_second = models.FloatField("Коэффициент на победу второй команды", default=0)
    coefficient_loss = models.FloatField("Коэффициент на ничью", default=0)

    def __str__(self):
        return f"{self.first_team}-{self.second_team}"
