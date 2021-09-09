from django.http import HttpResponseForbidden, HttpResponseRedirect

# 데코레이터 생성
# 현재 접속 중인 키와 접속하려는 페이지가 일치하는지 확인
from django.shortcuts import resolve_url

from profileapp.models import Profile


def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk'])
        if not profile.user == request.user:
            return HttpResponseRedirect(resolve_url('accountapp:hello_world'))
        return func(request, *args, **kwargs)
    return decorated