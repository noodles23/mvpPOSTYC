from django import forms

from .models import CustomerDB, alertbox

class NewCustomer(forms.ModelForm):
	class Meta:
		model = CustomerDB
		fields = ['customer_name', 'company_website', 'company_name',  'company_country',  'company_primary_currency',]
		### 'client',
	
	def clean_email(self):
		email = self.cleaned_data.get('merchant_email')
		email_base, provider = email.split("@")
		domain, extension = provider.split('.')
		return email

	def clean_product_name(self):
		product_name = self.cleaned_data.get('product_name')
		return product_name

class NewAlert(forms.ModelForm):
	class Meta:
		model = alertbox
		fields = ['alert_user', 'alert_type', 'alert_title',  'alert_text', 'alert_link',]