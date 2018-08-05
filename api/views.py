from rest_framework import generics
from classes.models import (Classroom)
from .serializers import ClassroomListSerializer

class ClassroomsList(generics.ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomListSerializer

class ClassroomDetail(generics.RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'

class ClassroomCreate(generics.CreateAPIView):
    serializer_class = ClassroomListSerializer

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


class ClassroomUpdateOrDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'