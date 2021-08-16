from django.urls import path
from .api_view import (
    PollListView,
    PollRetrieveView,
    PollCreateView,
    PollDeleteView,
    PollUpdateView,
)

app_name = 'main'

urlpatterns = [
    path('get/polls/', PollListView.as_view(), name='get_polls'),
    path('get/poll/<str:rand_title>', PollRetrieveView.as_view(), name='get_poll'),
    path('create/poll/', PollCreateView.as_view(), name='create_poll'),
    path('update/poll/<str:rand_title>/',
         PollUpdateView.as_view(), name='update_poll'),
    path('delete/poll/<str:rand_title>/',
         PollDeleteView.as_view(), name='delete_poll'),
]
