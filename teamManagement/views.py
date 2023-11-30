from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import TeamMemberForm
from .models import TeamMember


# Create your views here.

class TeamListView(ListView):
    model = TeamMember
    template_name = 'teamManagement/team_list.html'
    context_object_name = 'team_members'


class TeamAddView(CreateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'teamManagement/edit_member.html'
    success_url = '/'

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class TeamEditView(UpdateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'teamManagement/edit_member.html'
    success_url = '/'

    def get_object(self, queryset=None):
        return get_object_or_404(TeamMember, id=self.kwargs['member_id'])


class TeamDeleteView(DeleteView):
    model = TeamMember
    template_name = 'teamManagement/edit_member.html'  # Create a delete confirmation template
    success_url = '/'
