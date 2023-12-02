from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from teamManagement import views

app_name = 'teamManagement'

urlpatterns = [
    path('', csrf_exempt(views.LoginView.as_view()), name='login'),
    path('register', csrf_exempt(views.RegisterView.as_view()), name='register'),
    path('list', views.TeamListView.as_view(), name='team_list'),
    path('add', views.TeamAddView.as_view(), name='add_member'),
    path('edit/<int:member_id>', views.TeamEditView.as_view(), name='edit_member'),
    path('delete/<int:pk>', views.TeamDeleteView.as_view(), name='delete_member'),
    path('logout', csrf_exempt(views.user_logout), name='logout')
]
