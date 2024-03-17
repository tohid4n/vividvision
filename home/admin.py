from django.contrib import admin
from .models import DonationModel



class DonationModelAdmin(admin.ModelAdmin):
    list_display = ('amount', 'razor_pay_payment_id', 'is_paid') 

admin.site.register(DonationModel, DonationModelAdmin)