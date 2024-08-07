from django import forms
from .models import DonationModel

# List of currencies with their country names
CURRENCY_CHOICES = [
    ('USD', 'United States Dollar'),
    ('EUR', 'European Euro'),
    ('GBP', 'Pound Sterling'),
    ('SGD', 'Singapore Dollar'),
    ('AED', 'United Arab Emirates Dirham'),
    ('AUD', 'Australian Dollar'),
    ('CAD', 'Canadian Dollar'),
    ('CNY', 'Chinese Yuan Renminbi'),
    ('SEK', 'Swedish Krona'),
    ('NZD', 'New Zealand Dollar'),
    ('MXN', 'Mexican Peso'),
    ('HKD', 'Hong Kong Dollar'),
    ('NOK', 'Norwegian Krone'),
    ('RUB', 'Russian Ruble'),
    ('ALL', 'Albanian Lek'),
    ('AMD', 'Armenian Dram'),
    ('ARS', 'Argentine Peso'),
    ('AWG', 'Aruban Florin'),
    ('BBD', 'Barbadian Dollar'),
    ('BDT', 'Bangladeshi Taka'),
    ('BMD', 'Bermudian Dollar'),
    ('BND', 'Brunei Dollar'),
    ('BOB', 'Bolivian Boliviano'),
    ('BSD', 'Bahamian Dollar'),
    ('BWP', 'Botswana Pula'),
    ('BZD', 'Belize Dollar'),
    ('CHF', 'Swiss Franc'),
    ('COP', 'Colombian Peso'),
    ('CRC', 'Costa Rican Colon'),
    ('CUP', 'Cuban Peso'),
    ('CZK', 'Czech Koruna'),
    ('DKK', 'Danish Krone'),
    ('DOP', 'Dominican Peso'),
    ('DZD', 'Algerian Dinar'),
    ('EGP', 'Egyptian Pound'),
    ('ETB', 'Ethiopian Birr'),
    ('FJD', 'Fijian Dollar'),
    ('GIP', 'Gibraltar Pound'),
    ('GMD', 'Gambian Dalasi'),
    ('GTQ', 'Guatemalan Quetzal'),
    ('GYD', 'Guyanese Dollar'),
    ('HNL', 'Honduran Lempira'),
    ('HRK', 'Croatian Kuna'),
    ('HTG', 'Haitian Gourde'),
    ('HUF', 'Hungarian Forint'),
    ('IDR', 'Indonesian Rupiah'),
    ('ILS', 'Israeli New Shekel'),
    ('INR', 'Indian Rupee'),
    ('JMD', 'Jamaican Dollar'),
    ('KES', 'Kenyan Shilling'),
    ('KGS', 'Kyrgyzstani Som'),
    ('KHR', 'Cambodian Riel'),
    ('KYD', 'Cayman Islands Dollar'),
    ('KZT', 'Kazakhstani Tenge'),
    ('LAK', 'Lao Kip'),
    ('LBP', 'Lebanese Pound'),
    ('LKR', 'Sri Lankan Rupee'),
    ('LRD', 'Liberian Dollar'),
    ('LSL', 'Lesotho Loti'),
    ('MAD', 'Moroccan Dirham'),
    ('MDL', 'Moldovan Leu'),
    ('MKD', 'Macedonian Denar'),
    ('MMK', 'Myanmar Kyat'),
    ('MNT', 'Mongolian Tugrik'),
    ('MOP', 'Macanese Pataca'),
    ('MUR', 'Mauritian Rupee'),
    ('MVR', 'Maldivian Rufiyaa'),
    ('MWK', 'Malawian Kwacha'),
    ('MYR', 'Malaysian Ringgit'),
    ('NAD', 'Namibian Dollar'),
    ('NGN', 'Nigerian Naira'),
    ('NOK', 'Norwegian Krone'),
    ('NPR', 'Nepalese Rupee'),
    ('PEN', 'Peruvian Sol'),
    ('PGK', 'Papua New Guinean Kina'),
    ('PHP', 'Philippine Peso'),
    ('PKR', 'Pakistani Rupee'),
    ('QAR', 'Qatari Riyal'),
    ('SAR', 'Saudi Arabian Riyal'),
    ('SCR', 'Seychellois Rupee'),
    ('SLL', 'Sierra Leonean Leone'),
    ('SOS', 'Somali Shilling'),
    ('SSP', 'South Sudanese Pound'),
    ('SVC', 'Salvadoran Colon'),
    ('SZL', 'Swazi Lilangeni'),
    ('THB', 'Thai Baht'),
    ('TTD', 'Trinidad and Tobago Dollar'),
    ('TZS', 'Tanzanian Shilling'),
    ('UYU', 'Uruguayan Peso'),
    ('UZS', 'Uzbekistani Som'),
    ('YER', 'Yemeni Rial'),
    ('ZAR', 'South African Rand'),
    ('GHS', 'Ghanaian Cedi'),
]

class DonationForm(forms.ModelForm):
    amount = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.TextInput(attrs={'placeholder': 'Enter Amount'}))
    currency = forms.ChoiceField(choices=CURRENCY_CHOICES, widget=forms.Select(attrs={'placeholder': 'Choose Your Currency'}))

    class Meta:
        model = DonationModel
        fields = ['amount', 'currency']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['amount'].label = ""
        self.fields['currency'].label = ""
        
        self.fields['amount'].widget.attrs.update({"class": "text-xl font-Inter font-normal text-black w-80 xsm:w-96 px-8 py-5 border border-black focus:outline-none border-radius-50 mt-4"})
        self.fields['currency'].widget.attrs.update({"class": "text-xl font-Inter font-normal text-black w-80 xsm:w-96 px-8 py-5 border border-black focus:outline-none border-radius-50 mt-4"})
