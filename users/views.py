from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from lms.models import Course
from users.models import Payments, Subscriptions
from users.serializers.subscriptions import SubscriptionSerializer
from users.serializers.payments import PaymentsSerializer


class PaymentDateAPIListView(generics.ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['course', 'lesson', 'payment_method']
    ordering_field = ['payment_date']


class SubscriptionsAPIView(APIView):
    serializer_class = SubscriptionSerializer
    queryset = Payments.objects.all()

    def post(self, *args, **kwargs):

        user = self.request.user
        course_id = self.request.data.get('course')
        course_item = generics.get_object_or_404(Course, pk=course_id)

        subs_item, created = Subscriptions.objects.get_or_create(user=user, course=course_item)

        if created:
            message = 'You are now subscribed to this course'
        else:
            subs_item.delete()
            message = 'You are now unsubscribed from this course'

        return Response({"message": message})


