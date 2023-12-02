from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView

from .forms import TeamMemberForm, RegistrationForm, LoginForm
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
    success_url = '/list'

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class TeamEditView(UpdateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'teamManagement/edit_member.html'
    success_url = '/list'

    def get_object(self, queryset=None):
        return get_object_or_404(TeamMember, id=self.kwargs['member_id'])


class TeamDeleteView(DeleteView):
    model = TeamMember
    template_name = 'teamManagement/edit_member.html'  # Create a delete confirmation template
    success_url = '/list'


class RegisterView(SuccessMessageMixin, FormView):
    template_name = 'teamManagement/register.html'
    form_class = RegistrationForm
    success_url = 'list'  # Redirect to the list page after successful registration
    success_message = "Registration successful. You are now logged in."

    def form_valid(self, form):
        # Save the form data and log in the user
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'teamManagement/login.html'
    form_class = LoginForm
    success_url = 'list'  # Redirect to home page after successful login

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user:
            login(self.request, user)
        return super().form_valid(form)


def user_logout(request):
    logout(request)
    return redirect('/')
