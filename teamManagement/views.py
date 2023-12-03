from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView

from .forms import TeamMemberForm, RegistrationForm, LoginForm
from .models import TeamMember


# Create your views here.


# Team members List View
class TeamListView(ListView):
    model = TeamMember
    template_name = 'teamManagement/team_list.html'
    context_object_name = 'team_members'


# Team member Add view
class TeamAddView(CreateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'teamManagement/add_edit_member.html'
    success_url = '/list'

    def form_valid(self, form):
        # Access the logged-in user
        user = self.request.user

        # Access the selected role from the form
        selected_role = form.cleaned_data.get('role')

        # Check if the user is an admin
        if not user.role == 'admin' and selected_role == 'admin':
            form.add_error('role', 'Regular users can only select the "regular" role.')
            return self.form_invalid(form)
        # Continue with the default behavior of the parent class
        return super().form_valid(form)


# Team Member Edit View
class TeamEditView(UpdateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'teamManagement/add_edit_member.html'
    success_url = '/list'

    def get_object(self, queryset=None):
        return get_object_or_404(TeamMember, id=self.kwargs['member_id'])


# Team Member Delete View
class TeamDeleteView(DeleteView):
    model = TeamMember
    template_name = 'teamManagement/add_edit_member.html'  # Create a delete confirmation template
    success_url = '/list'


# Register Team Member/User View
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


# Login Team Member/User View
class LoginView(FormView):
    template_name = 'teamManagement/login.html'
    form_class = LoginForm
    success_url = 'list'  # Redirect to home page after successful login

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user:
            login(self.request, user)
        return super().form_valid(form)


# Logout view
def user_logout(request):
    logout(request)
    return redirect('/')
