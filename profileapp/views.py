from django.urls import reverse_lazy

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile

from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView


class ProfileCreateView(CreateView):
    model=Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp:create.html'