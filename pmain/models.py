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

class subchart(models.Model):
	chart_name = models.CharField(max_length=120, blank=True, null=True)
	chart_title = models.CharField(max_length=600, blank=True, null=True)
	chart_id = models.CharField(max_length=600, blank=True, null=True)
	chart_exp = models.CharField(max_length=2000, blank=True, null=True)
	chart_base = models.CharField(max_length=600, blank=True, null=True)
	chart_parent_id = models.CharField(max_length=600, blank=True, null=True)
	def __unicode__(self): #Python 3.3 is __str__
		return self.chart_id

class custtouchpoint(models.Model):
	cust_email2 = models.CharField(max_length=2000, blank=False, null=False)
	touchpoint_type = models.CharField(max_length=300, blank=False, null=False)
	touchpoint_datasource = models.CharField(max_length=200, blank=True, null=True)
	touchpoint_background = models.CharField(max_length=200, blank=True, null=True)
	touchpoint_date = models.CharField(max_length=100, blank=True, null=True)
	touchpoint_month = models.CharField(max_length=100, blank=True, null=True)
	touchpoint_name = models.CharField(max_length=200, blank=True, null=True)
	touchpoint_owner = models.CharField(max_length=100, blank=True, null=True)
	touchpoint_category = models.CharField(max_length=200, blank=True, null=True)
	touchpoint_amount = models.CharField(max_length=200, blank=True, null=True)
	touchpoint_count = models.CharField(max_length=100, blank=True, null=True)
	def __unicode__(self): #Python 3.3 is __str__
		return self.cust_email2

# class custdb(models.Model):
# 	cust_name = models.CharField(max_length=120, blank=False, null=False)
# 	cust_id = models.CharField(max_length=120, blank=False, null=False)
# 	cust_email = models.CharField(max_length=2000, blank=False, null=False)
# 	cust_table = models.CharField(max_length=200, blank=False, null=False)
# 	cust_gender = models.CharField(max_length=600, blank=True, null=True)
# 	cust_agegroup = models.CharField(max_length=600, blank=True, null=True)
# 	cust_address = models.CharField(max_length=2000, blank=True, null=True)
# 	cust_state = models.CharField(max_length=600, blank=True, null=True)
# 	cust_country = models.CharField(max_length=100, blank=True, null=True)
# 	cust_status = models.CharField(max_length=100, blank=True, null=True)
# 	cust_special = models.CharField(max_length=100, blank=True, null=True)
# 	cust_referredby = models.CharField(max_length=120, blank=True, null=True)
# 	cust_referredRoot = models.CharField(max_length=120, blank=True, null=True)
# 	cust_joindate = models.CharField(max_length=100, blank=True, null=True)
# 	cust_lastactive = models.CharField(max_length=100, blank=True, null=True)
# 	def __unicode__(self): #Python 3.3 is __str__
# 		return self.cust_email

class alertbox(models.Model):
	alert_user = models.ForeignKey(settings.AUTH_USER_MODEL)
	alert_type = models.CharField(max_length=100, blank=True, null=True)
	alert_title = models.CharField(max_length=600, blank=True, null=True)
	alert_text = models.CharField(max_length=2000, blank=True, null=True)
	alert_link = models.CharField(max_length=600, blank=True, null=True)
	alert_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	alert_2 = models.CharField(max_length=600, blank=True, null=True)
	alert_3 = models.CharField(max_length=600, blank=True, null=True)
	def __unicode__(self): #Python 3.3 is __str__
		return self.alert_title

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