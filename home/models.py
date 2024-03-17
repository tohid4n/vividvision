from django.db import models

class DonationModel(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    is_paid = models.BooleanField(default=False)
    razor_pay_order_id = models.CharField(max_length=100, null=True, blank=True)
    razor_pay_payment_id = models.CharField(max_length=100, null=True, blank=True)
    razor_pay_payment_id_signature = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.amount} {self.currency}'

    
    
    
