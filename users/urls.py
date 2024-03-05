from django.urls import path

from users.views import PaymentDateAPIListView

urlpatterns = [
    path('payments/', PaymentDateAPIListView.as_view())
]
