from django.http import HttpResponseForbidden

# 데코레이터 생성
# 현재 접속 중인 키와 접속하려는 페이지가 일치하는지 확인
from articleapp.models import Article


def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk'])
        if not article.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated