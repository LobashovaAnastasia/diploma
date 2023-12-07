from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main),
    # FIXME: tournaments/<int:tournament_id>  (множественное число - tournamentS)
    path('main/tournament/<int:tournament_id>', views.tournament_info),
    # FIXME: почему этот энд-поинт в сегмементе tournament? Он вытаскивает данные по команде и игрокам.
    path('main/tournament/team_info/<int:team_id>', views.team_info),

    # FIXME: player_info никак не связан ни турниром, ни с командой, ведь фильтрация идет сугубо по player_id
    path('main/tournament/team_info/player_info/<int:player_id>', views.player),

    # FIXME: я бы еще добавил эндпоинты для ВСЕХ команд и ВСЕХ игроков
    path('main/news', views.all_news),
    path('main/news/<int:news_id>', views.news),

    path('main/tournament/news/<int:tournament_id>', views.tournament_news),
    path('main/tournament/statistics/<int:tournament_id>', views.statistics),
    path('main/tournament/matches/<int:tournament_id>', views.list_of_matches),

    path('main/national_team', views.national_team),   # checked
    path('matches/results/', views.results),   # FIXME: для чего этот хэндлер?
]


