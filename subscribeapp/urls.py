
from django.urls import include, path
from projectapp.views import ProjectCreateView

from subscribeapp.models import Subscription
from subscribeapp.views import SubscriptionListView, SubscriptionView

app_name = "subscribeapp"

urlpatterns = [
    path('subcribe/', SubscriptionView.as_view(), name='subscribe'),
    path('list/', SubscriptionListView.as_view(), name='list'),


]
