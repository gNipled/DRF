from django.urls import path

from users.views import PaymentDateAPIListView, SubscriptionsAPIView

urlpatterns = [
    path('payments/', PaymentDateAPIListView.as_view()),
    path('subscriptions/', SubscriptionsAPIView.as_view(), name='subscribe'),
]
