from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from lms.models import Course, Lesson
from users.models import User, Subscriptions


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test@test.com',
            password='12345'
        )
        self.client.force_authenticate(
            user=self.user
        )
        self.course = Course.objects.create(
            name='test',
            owner=self.user
        )

        self.lesson = Lesson.objects.create(
            name='test',
            course=self.course,
            owner=self.user
        )

    def test_get_list(self):
        """Test for getting list of lessons"""

        response = self.client.get(
            '/lms/?page=1',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.lesson.id,
                        "name": self.lesson.name,
                        "description": self.lesson.description,
                        "preview": self.lesson.preview,
                        "video_link": self.lesson.video_link,
                        "course": self.lesson.course_id,
                        "owner": self.lesson.owner_id
                    }]
            }
        )

    def test_lesson_create(self):
        """Test of creation"""
        data = {
            'name': 'test2',
            'course': self.course.id
        }

        response = self.client.post(
            '/lms/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Lesson.objects.all().count(),
            2
        )

    def test_lesson_create_validation_error(self):
        """Test for validation error"""
        data1 = {
            'name': 'test2',
            'course': self.course.id,
            'video_link': 'yoububuf.,dsffsdgsdkjk23kjhlkafdyoutu.be'
        }
        data2 = {
            'name': 'test2',
            'course': self.course.id,
            'video_link': 'yoububuf.,dsffsdgsdkjk23kjhlkafdyou'
        }

        response = self.client.post(
            '/lms/create/',
            data=data1
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        response = self.client.post(
            '/lms/create/',
            data=data2
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_lesson_detail(self):
        response = self.client.get(
            f'/lms/{self.lesson.id}/'
        )

        self.assertEqual(
            response.json(),
            {
                "id": self.lesson.id,
                "name": self.lesson.name,
                "description": self.lesson.description,
                "preview": self.lesson.preview,
                "video_link": self.lesson.video_link,
                "course": self.lesson.course_id,
                "owner": self.lesson.owner_id
            }
        )

    def test_lesson_update(self):

        data = {
            "name": "updated_name",
            "description": "updated_description"
        }
        response = self.client.patch(
            f'/lms/{self.lesson.id}/update/',
            data=data
        )

        self.assertEqual(
            response.json(),
            {
                "id": self.lesson.id,
                "name": "updated_name",
                "description": "updated_description",
                "preview": self.lesson.preview,
                "video_link": self.lesson.video_link,
                "course": self.lesson.course_id,
                "owner": self.lesson.owner_id
            }
        )

    def test_lesson_delete(self):
        response = self.client.delete(
            f'/lms/{self.lesson.id}/delete/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


