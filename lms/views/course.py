from rest_framework.viewsets import ModelViewSet

from lms.models import Course
from lms.paginators import CoursePaginator
from lms.serializers.course import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CoursePaginator
