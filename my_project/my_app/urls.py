from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main),
    path('main/tournaments/<int:tournament_id>', views.tournament_info),
    path('main/tournaments/team_info/<int:team_id>', views.team_info),
    path('main/tournaments/team_info/player_info/<int:player_id>', views.get_player_by_id),
    path('main/news', views.get_all_news),
    path('main/news/<int:news_id>', views.get_news_by_id),
    path('main/tournaments/news/<int:tournament_id>', views.get_tournament_news),
    path('main/tournaments/statistics/<int:tournament_id>', views.statistics),
    path('main/tournaments/matches/<int:tournament_id>', views.list_of_matches),
    path('main/national_team', views.national_team),
]


