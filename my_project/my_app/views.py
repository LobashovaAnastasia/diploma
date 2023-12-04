from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import Tournament, Team, Player, News, Match
from datetime import datetime


def _get_all_tournaments():
    queryset = Tournament.objects.select_related()

    tournaments = []
    for tournament in queryset:
        tournaments.append(
            {
                'id': tournament.id,
                'name': tournament.name,
                'logo': tournament.logo
            }
        )

    return tournaments


def _get_all_teams():
    queryset = Team.objects.select_related()

    teams = []
    for team in queryset:
        teams.append(
            {
                'id': team.id,
                'name': team.name,
                'points': team.points,
                'tournament': team.tournament,
                'goals': team.goals,
                'conceded': team.conceded,
                'info': team.info,
                'team_logo': team.team_logo,
                'win': team.win,
                'loss': team.loss,
                'draw': team.draw
            }
        )

    return teams


def _get_last_two_news():
    queryset = News.objects.select_related().order_by('-date')[:2]

    return queryset


def _all_news():
    queryset = News.objects.select_related().order_by('-date')

    return queryset


def tournament_news(request: HttpRequest, tournament_id) -> HttpResponse:

    news_list = News.objects.filter(category=tournament_id)

    data = {'news_list': news_list}

    return render(request, "news_list.html", context=data)


def _get_last_two_matches():
    queryset = Match.objects.filter(time__lte=datetime.now()).order_by('-time')[:2]

    return queryset


def main(request: HttpRequest) -> HttpResponse:
    news_list = _get_last_two_news()

    matches = _get_last_two_matches()

    data = {'news_list': news_list, 'list_of_matches': matches}

    return render(request, "main.html", context=data)


def all_news(request: HttpRequest) -> HttpResponse:
    news_list = _all_news()

    data = {'news_list': news_list}

    return render(request, 'news_list.html', context=data)


def news(request: HttpRequest, news_id: int) -> HttpResponse:
    if not (news := News.objects.filter(id=news_id).first()):
        return HttpResponseNotFound(f"The news does not exist")

    data = {'news': news}

    return render(request, "news.html", context=data)


def tournament_info(request: HttpRequest, tournament_id: int) -> HttpResponse:
    if not (tournament := Tournament.objects.filter(id=tournament_id).first()):
        return HttpResponseNotFound(f"The tournament does not exist")

    teams = Team.objects.filter(tournament=tournament).order_by('-points')

    data = {'tournament': tournament, 'teams': teams}

    return render(request, "tournament.html", context=data)


def national_team(request: HttpRequest) -> HttpResponse:
    tournament = Tournament.objects.get(name='Национальная сборная')

    news_list = News.objects.filter(category=tournament)

    matches = Match.objects.filter(first_team__in=tournament.teams.all()).order_by('time')[:4]

    data = {'news_list': news_list, "tournament": tournament, "matches": matches}

    return render(request, "national_team.html", context=data)


def team_info(request: HttpRequest, team_id: int) -> HttpResponse:
    teams = Team.objects.filter(id=team_id).first()

    players = Player.objects.filter(team=teams)

    data = {'info': teams, 'players': players}

    return render(request, "team_info.html", context=data)


def statistics(request: HttpRequest, tournament_id: int) -> HttpResponse:
    players = Player.objects.filter(team__tournament_id=tournament_id).order_by('-goals')[:10]

    data = {"players": players}

    return render(request, "statistics.html", context=data)


def list_of_matches(request: HttpRequest, tournament_id: int) -> HttpResponse:
    tournament = Tournament.objects.get(id=tournament_id)

    matches = Match.objects.filter(first_team__in=tournament.teams.all()).order_by('-time')

    data = {'tournament': tournament, 'matches': matches}

    return render(request, "list_of_matches.html", context=data)


def results(request: HttpRequest):
    return HttpResponse("Results")


def player(request: HttpRequest, player_id: int):
    player_info = Player.objects.filter(id=player_id).first()

    data = {'player': player_info}

    return render(request, "player_info.html", context=data)
