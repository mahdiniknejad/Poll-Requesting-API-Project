from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .models import Poll
from .serializers import PollSerializer


class PollListView(ListAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()


class PollObjectView(RetrieveAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
    lookup_field = "rand_title"


class PollCreateView(CreateAPIView):
    serializer_class = PollSerializer
