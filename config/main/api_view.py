# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status
from .models import Poll
from .serializers import PollSerializer


class PollListView(ListAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()


# class PollAPIView(APIView):
#     # serializer_class = PollSerializer

#     def get(self, request):
#         _data = Poll.objects.all()
#         serialized_data = PollSerializer(instance=_data, many=True)
#         return Response(serialized_data.data, status.HTTP_200_OK)

#     def post(self):
#         pass
