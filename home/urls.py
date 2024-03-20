from django.urls import path
from .views import HomePageView, About, Contact, PrivacyAndPolicy, TermsAndConditions, RefundPolicies


app_name = 'home'


urlpatterns = [
    path('', HomePageView.as_view(), name="home-page"),
    path('about-us/', About.as_view(), name="about-us"),
    path('contact-us/', Contact.as_view(), name="contact-us"),
    path('privacy-and-policy/', PrivacyAndPolicy.as_view(), name="privacy-policy"),
    path('terms-and-conditions/', TermsAndConditions.as_view(), name="terms-and-conditions"),
    path('refund-policies/', RefundPolicies.as_view(), name="refund-policies"),
    # path('payment/<int:donation_id>/', PaymentView.as_view(), name="payment-page"),
    # path('payment/success/', success, name="payment-success"),
]
