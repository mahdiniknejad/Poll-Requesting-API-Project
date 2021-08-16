from .models import Poll
from .serializers import PollSerializer
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
)


class PollListView(ListAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()


class PollRetrieveView(RetrieveAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
    lookup_field = "rand_title"


class PollCreateView(CreateAPIView):
    serializer_class = PollSerializer


class PollDeleteView(DestroyAPIView):
    queryset = Poll.objects.all()
    lookup_field = "rand_title"


class PollUpdateView(UpdateAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
    lookup_field = "rand_title"
