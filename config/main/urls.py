from django.urls import path
from .api_view import PollListView

app_name = 'main'

urlpatterns = [
    path('get/polls/', PollListView.as_view(), name='get_polls'),
]
