from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.conf import settings

# Create your models here.
class CustomerDB(models.Model):
	customer_name = models.CharField(max_length=600, blank=False, null=False)
	company_website = models.CharField(max_length=600, blank=False, null=False)
	company_name = models.CharField(max_length=600, blank=False, null=False)
	company_country = models.CharField(max_length=600, blank=False, null=False)
	company_primary_currency = models.CharField(max_length=600, blank=False, null=False)
	customer_status = models.CharField(max_length=100, blank=True, null=True)
	form_status = models.CharField(max_length=100, blank=False, null=False)
	customer_username = models.CharField(max_length=100, blank=False, null=False)
	customer_email = models.EmailField(blank=False, null=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	def __unicode__(self):
		return self.customer_name

# class DataSources(models.Model):
# 	data_source_name = models.CharField(max_length=600, blank=False, null=False)
# 	data_source_type = models.CharField(max_length=600, blank=False, null=False)
# 	data_source_status = models.CharField(max_length=200, blank=False, null=False)
# 	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
# 	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
# 	def __unicode__(self):
# 		return self.data_source_name

# class CustomerDataSources(models.Model):
# 	customer_id = models.CharField(max_length=600, blank=False, null=False)
# 	customer_email = models.CharField(max_length=600, blank=False, null=False)
# 	customer_username = models.CharField(max_length=600, blank=False, null=False)
# 	data_source_type = models.ForeignKey(DataSources, blank=False, null=False)
# 	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
# 	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
# 	def __unicode__(self):
# 		return self.customer_name

	# MAIN CustomerDB
	# customer_name
	# website
	# company_name
	# company_country
	# company_currency
	# customer_status (initial, waiting, active, admin)

	# customer_data_sources
	# USE REGISTRATION EMAIL AS ForeignKey
	# customer_email
	# Data_Web_analytics
	# Data_Ecomm_Platform
	# Data_CRM