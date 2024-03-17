from django.urls import path
from .views import HomePageView, PaymentView, success


app_name = 'home'


urlpatterns = [
    path('', HomePageView.as_view(), name="home-page"),
    path('payment/<int:donation_id>/', PaymentView.as_view(), name="payment-page"),
    path('payment/success/', success, name="payment-success"),
]


