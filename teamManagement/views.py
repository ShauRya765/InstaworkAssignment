from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import TeamMember


# Create your views here.

class TeamListView(ListView):
    model = TeamMember
    template_name = 'teamManangement/team_members.html'
    context_object_name = 'team_members'
