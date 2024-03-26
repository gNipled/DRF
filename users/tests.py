from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from lms.models import Course
from users.models import User, Subscriptions


class SubscriptionsTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.com', password='12345')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(name="test", owner=self.user)
        self.subscription = Subscriptions.objects.create(users=self.user, course=self.course)

    def test_create_subscription(self):
        data = {
            "users": self.user.id,
            "course": self.course.id,
        }

        response = self.client.post(
            '/users/subscriptions/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'message': 'You are now unsubscribed from this course'}
        )
