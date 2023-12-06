import sys

from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from my_app.utils import query_debugger
from my_app.models import Tournament, Team, Player, News, Match
from datetime import datetime
import logging


logging.basicConfig(
    format="%(asctime)s.%(msecs)03d %(levelname)s "
    "[%(name)s:%(funcName)s:%(lineno)s] -> %(message)s",
    datefmt="%Y-%m-%d,%H:%M:%S",
    stream=sys.stdout,
    level=logging.DEBUG,
)
logger = logging.getLogger(__name__)

django_logger = logging.getLogger("django.db.backends")
django_logger.setLevel(logging.DEBUG)
django_logger.addHandler(logging.StreamHandler())


@query_debugger(logger)
def _get_all_tournaments():

    return list(Tournament.objects.select_related().values())


@query_debugger(logger)
def _get_all_teams():

    return list(Team.objects.select_related().values())


@query_debugger(logger)
def get_tournament_news(request: HttpRequest, tournament_id) -> HttpResponse:
    news_list = News.objects.filter(category=tournament_id)
    data = {'news_list': news_list}

    return render(request, "news_list.html", context=data)


@query_debugger(logger)
def main(request: HttpRequest) -> HttpResponse:
    news_list = News.objects.select_related().order_by('-date')[:2]
    matches = Match.objects.select_related().filter(time__lte=datetime.now()).order_by('-time')[:2]
    data = {'news_list': news_list, 'list_of_matches': matches}

    return render(request, "main.html", context=data)


@query_debugger(logger)
def get_all_news(request: HttpRequest) -> HttpResponse:
    news_list = News.objects.select_related().order_by('-date')
    data = {'news_list': news_list}

    return render(request, 'news_list.html', context=data)


@query_debugger(logger)
def get_news_by_id(request: HttpRequest, news_id: int) -> HttpResponse:
    if not (news := News.objects.select_related().filter(id=news_id).first()):
        return HttpResponseNotFound(f"The news does not exist")

    data = {'news': news}

    return render(request, "news.html", context=data)


@query_debugger(logger)
def tournament_info(request: HttpRequest, tournament_id: int) -> HttpResponse:
    if not (tournament := Tournament.objects.filter(id=tournament_id).first()):
        return HttpResponseNotFound(f"The tournament by id {tournament_id} does not exist")
    teams = Team.objects.select_related().filter(tournament__pk=tournament_id).order_by('-points')
    data = {'tournament': tournament, 'teams': teams}

    return render(request, "tournament.html", context=data)


@query_debugger(logger)
def national_team(request: HttpRequest) -> HttpResponse:
    if not (tournament := Tournament.objects.filter(name='Национальная сборная').first()):
        return HttpResponseNotFound(f"The national team does not exist")
    news_list = News.objects.select_related().filter(category=tournament)
    matches = Match.objects.select_related().filter(first_team__in=tournament.teams.all()).order_by('time')[:4]
    data = {'news_list': news_list, "tournament": tournament, "matches": matches}

    return render(request, "national_team.html", context=data)


@query_debugger(logger)
def team_info(request: HttpRequest, team_id: int) -> HttpResponse:
    if not (teams := Team.objects.filter(id=team_id).first()):
        return HttpResponseNotFound(f"The team by id {team_id} does not exist")
    players = Player.objects.filter(team=teams)
    data = {'info': teams, 'players': players}

    return render(request, "team_info.html", context=data)


@query_debugger(logger)
def statistics(request: HttpRequest, tournament_id: int) -> HttpResponse:
    players = Player.objects.select_related().filter(team__tournament_id=tournament_id).order_by('-goals')[:10]
    data = {"players": players}

    return render(request, "statistics.html", context=data)


@query_debugger(logger)
def list_of_matches(request: HttpRequest, tournament_id: int) -> HttpResponse:
    if not (tournament := Tournament.objects.filter(id=tournament_id).first()):
        return HttpResponseNotFound(f"The tournament by id {tournament_id} does not exist")
    matches = Match.objects.select_related().filter(first_team__in=tournament.teams.all()).order_by('-time')
    data = {'tournament': tournament, 'matches': matches}

    return render(request, "list_of_matches.html", context=data)


@query_debugger(logger)
def get_player_by_id(request: HttpRequest, player_id: int):
    if not (player_info := Player.objects.select_related().filter(id=player_id).first()):
        return HttpResponseNotFound(f"The player by id {player_id} does not exist")
    data = {'player': player_info}

    return render(request, "player_info.html", context=data)
