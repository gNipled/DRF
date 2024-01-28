from django.urls import path
from rest_framework import routers

from lms.views.course import CourseViewSet
from lms.views.lesson import LessonListView, LessonCreateView, LessonDestroyView, LessonDetailView, LessonUpdateView

urlpatterns = [
    path('', LessonListView.as_view()),
    path('create/', LessonCreateView.as_view()),
    path('<int:pk>/delete/', LessonDestroyView.as_view()),
    path('<int:pk>/', LessonDetailView.as_view()),
    path('<int:pk>/update/', LessonUpdateView.as_view()),
]


router = routers.SimpleRouter()
router.register('course', CourseViewSet)

urlpatterns += router.urls
