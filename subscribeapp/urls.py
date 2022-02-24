
from django.urls import include, path

from projectapp.views import ProjectCreateView

app_name = "subscribeapp"

urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='create'),
    

]
