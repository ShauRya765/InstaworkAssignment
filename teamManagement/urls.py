from django.urls import path
from teamManagement import views

app_name = 'teamManagement'

urlpatterns = [
    path('', views.TeamListView.as_view(),name='list_team')
]
