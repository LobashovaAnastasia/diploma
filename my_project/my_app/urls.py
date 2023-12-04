from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main),
    path('main/tournament/<int:tournament_id>', views.tournament_info),
    path('main/tournament/team_info/<int:team_id>', views.team_info),
    path('main/tournament/team_info/player_info/<int:player_id>', views.player),
    path('main/news', views.all_news),
    path('main/news/<int:news_id>', views.news),
    path('main/tournament/news/<int:tournament_id>', views.tournament_news),
    path('main/tournament/statistics/<int:tournament_id>', views.statistics),
    path('main/tournament/matches/<int:tournament_id>', views.list_of_matches),

    path('main/national_team', views.national_team),
    path('matches/results/', views.results),
]


