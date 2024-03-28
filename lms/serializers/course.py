from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from lms.models import Course, Lesson
from users.models import Subscriptions


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = SerializerMethodField()
    lessons_in_course = SerializerMethodField()
    is_subscribed = SerializerMethodField()

    def get_lesson_count(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_lessons_in_course(self, course):
        return [lesson.name for lesson in Lesson.objects.filter(course=course)]

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return Subscriptions.objects.filter(user=user, course=obj).exists()
        return False

    class Meta:
        model = Course
        fields = ('name', 'lesson_count', 'lessons_in_course', 'is_subscribed')
