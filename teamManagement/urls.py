from django.urls import path
from teamManagement import views

app_name = 'teamManagement'

urlpatterns = [
    path('', views.TeamListView.as_view(), name='team_list'),
    path('add', views.TeamAddView.as_view(), name='add_member'),
    path('edit/<int:member_id>', views.TeamEditView.as_view(), name='edit_member'),
    path('delete/<int:pk>', views.TeamDeleteView.as_view(), name='delete_member')
]
