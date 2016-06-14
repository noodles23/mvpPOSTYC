from django.db import models

# Create your models here.
class cust_db_model(models.Model):
	user_current = models.CharField(max_length=600, blank=False, null=False)
	db_host = models.CharField(max_length=600, blank=True, null=True)
	db_name = models.CharField(max_length=600, blank=False, null=False)
	db_table = models.CharField(max_length=600, blank=False, null=False)
	db_username = models.CharField(max_length=600, blank=False, null=False)
	db_password = models.CharField(max_length=600, blank=False, null=False)
	def __unicode__(self): #Python 3.3 is __str__
		return self.user_current
