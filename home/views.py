import decimal
import requests
import razorpay
from django.http import  HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.conf import settings
from .forms import DonationForm
from django.shortcuts import get_object_or_404
from .models import DonationModel
from django.shortcuts import render


# class HomePageView(generic.FormView):
#     form_class = DonationForm
#     template_name = 'home-page.html'

#     def form_valid(self, form):
#         form.save()  # Save the donation form data
#         donation = form.instance  # Access the created donation object
#         return HttpResponseRedirect(reverse('home:payment-page', kwargs={'donation_id': donation.id}))  # Redirect to payment with donation ID



class HomePageView(generic.TemplateView):
    template_name = "home-page.html"
    

class PrivacyAndPolicy(generic.TemplateView):
    template_name = "privacy-policy.html"    
    
    
class TermsAndConditions(generic.TemplateView):
    template_name = "terms-and-conditions.html"
    
    
class RefundPolicies(generic.TemplateView):
    template_name = "refund-policies.html"        
    
    
class About(generic.TemplateView):
    template_name = "about-us.html"
    
class Contact(generic.TemplateView):
    template_name = "contact-us.html"
    
    
    
        
# class PaymentView(generic.TemplateView):
#     template_name = 'payment.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         donation_id = self.kwargs.get('donation_id')  # Get donation ID from URL pattern
#         donation = get_object_or_404(DonationModel, id=donation_id)

#         amount_inr = float(self.convert_to_inr(donation.amount, donation.currency))

#         client = razorpay.Client(auth=(settings.KEY_ID, settings.KEY_SECRET))
#         data = { "amount": int(amount_inr * 100), "currency": "INR" }  # Amount in paise
#         payment = client.order.create(data=data)
#         donation.razor_pay_order_id = payment['id']
#         donation.save()
#         context['donation'] = donation
#         context['payment'] = payment
#         context['key_id'] = settings.KEY_ID
#         return context


#     def convert_to_inr(self, amount, currency):
#         # Make a request to Open Exchange Rates API to get the latest exchange rates
#         response = requests.get(
#             f'https://open.er-api.com/v6/latest/{currency}',
#             params={'app_id': settings.OPEN_EXCHANGE_RATES_APP_ID}
#         )
#         data = response.json()

#         try:
#             # Check for successful response and valid 'rates' key
#             if response.status_code == 200 and 'rates' in data:
#                 inr_rate = data['rates']['INR']  # Access INR exchange rate

#                 # Ensure inr_rate is a decimal before multiplication
#                 inr_rate = decimal.Decimal(str(inr_rate))
#                 amount_inr = amount * inr_rate
#                 return amount_inr
#             else:
#                 print(f"Error getting exchange rates: {data}")
#                 # Handle error (e.g., display message to user)
#                 return None  # Or handle error in your view logic

#         except (requests.exceptions.RequestException, KeyError):
#             print(f"Error fetching exchange data from Open Exchange Rates")
#             # Handle API call error (e.g., display message to user)
#             return None  # Or handle error in your view logic
  

  
  
# def success(request):
#     razor_pay_order_id = request.GET.get('razorpay_order_id')
#     razorpay_payment_id = request.GET.get('razorpay_payment_id')
#     razorpay_signature = request.GET.get('razorpay_signature')
#     donation = get_object_or_404(DonationModel, razor_pay_order_id=razor_pay_order_id)
#     donation.is_paid = True
#     donation.razor_pay_payment_id = razorpay_payment_id
#     donation.razor_pay_payment_id_signature = razorpay_signature
#     donation.save()
#     return render(request, 'payment-success.html')

