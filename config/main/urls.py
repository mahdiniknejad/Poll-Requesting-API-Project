from django.urls import path
from .api_view import PollListView, PollObjectView, PollCreateView

app_name = 'main'

urlpatterns = [
    path('get/polls/', PollListView.as_view(), name='get_polls'),
    path('create/poll/', PollCreateView.as_view(), name='create_poll'),
    path('get/poll/<str:rand_title>', PollObjectView.as_view(), name='get_poll'),
]
