from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from users.views import PaymentDateAPIListView

urlpatterns = [
    path('payments/', PaymentDateAPIListView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh', TokenObtainPairView.as_view())
]
