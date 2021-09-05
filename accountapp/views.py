from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld
from django.http import HttpResponse
from django.shortcuts import redirect, render, resolve_url
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView


# 배열 내부에 데코레이터를 넣어 사용 가능
has_ownership = [account_ownership_required, login_required]

# Create your views here.
@login_required # 데코레이터 사용 -> 로그인 여부 확인 데코레이터
def hello_world(request):

        if request.method == "POST":
            temp = request.POST.get('hello_world_input')

            new_hello_world = HelloWorld()
            new_hello_world.text = temp
            new_hello_world.save()

            return HttpResponseRedirect(resolve_url('accountapp:hello_world'))

        else:
            hello_world_list = HelloWorld.objects.all()

            return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})






class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

@method_decorator(has_ownership, 'get')  #일반 펑션에 사용하는 데코레이터를 메소드에 사용 할 수 있도록 변환
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
