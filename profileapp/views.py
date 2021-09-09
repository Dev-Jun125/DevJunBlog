from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile

from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, UpdateView


class ProfileCreateView(CreateView):
    model=Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:detail')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit = False) # 사용자로 부터 받은 form 정보를 임시 저장
        temp_profile.user = self.request.user # 유저를 요청을 보낸 사람으로 설정
        temp_profile.save() # 저장
        return super().form_valid(form) # 부모에게게 리턴
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model=Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})
