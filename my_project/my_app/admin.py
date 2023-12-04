from django.contrib import admin
from .models import Team, Match, Player, Tournament, News

admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Player)
admin.site.register(Tournament)
admin.site.register(News)
