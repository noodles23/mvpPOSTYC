from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

CATEGORIES = (
        ('Google Analytics', 'Google Analytics'),
        ('Mailchimp', 'Mailchimp'),
        ('Shopify', 'Shopify'),
        ('Facebook', 'Facebook'),
        ('SugarCRM', 'SugarCRM'),
        ('ExactTarget', 'ExactTarget'),
        ('WooCommerce', 'WooCommerce'),)

CONNTYPE = (
        ('API Key', 'API Key'),
        ('Username Password', 'Username Password'),)


class Conn(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=200, default= 'Google Analytics', choices=CATEGORIES)
    connection_type = models.CharField(max_length=200, default= 'API', choices=CONNTYPE)
    username_or_apikey = models.CharField(max_length=600, blank=False, null=False, default= 'Username / API Key')
    password_if_required = models.CharField(max_length=600, blank=True, null=True, default= 'Password (If Required)')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('conn_edit', kwargs={'pk': self.pk})
