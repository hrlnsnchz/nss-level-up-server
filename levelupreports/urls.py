from django.urls import path
from .views.users.gamesbyuser import usergame_list

urlpatterns = [
    path('reports/usergames', usergame_list),
]