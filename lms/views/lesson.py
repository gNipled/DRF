from rest_framework.generics import RetrieveAPIView, DestroyAPIView, ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from lms.models import Lesson
from lms.paginators import LessonPaginator
from lms.permissions import IsOwner, IsModerator
from lms.serializers.lesson import LessonSerializer


class LessonDetailView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class LessonDestroyView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner & ~IsModerator]


class LessonListView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = LessonPaginator
    permission_classes = IsAuthenticated


class LessonCreateView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]


class LessonUpdateView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]
