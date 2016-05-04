from django.shortcuts import render, get_object_or_404, redirect

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import NewCustomer
from .models import CustomerDB

# Create your views here.

def home(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('auth_login'))
	else:
		return render(request, "home.html", {})

def profile(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('auth_login'))
	else:
		form = NewCustomer(request.POST or None)
		if request.method == 'POST' and form.is_valid():
			stock = form.save(commit=False)
			stock.customer_username = request.user
			stock.customer_email = request.user.email
			stock.form_status = 'completed'
			stock.save()
			return HttpResponseRedirect(reverse('home'))
		else:
			try: 
				search_id = request.user
				queryset = CustomerDB.objects.filter(customer_username=search_id).latest('timestamp')
				form = NewCustomer(
					request.POST or None,
					initial={'customer_name': queryset.customer_name, 'company_website': queryset.company_website, 'company_name': queryset.company_name, 'company_country': queryset.company_country, 'company_primary_currency': queryset.company_primary_currency, }
					)
				context = {
					"form": form,
					"queryset": queryset,
				}
				return render(request, "profile.html", context)
			except:
				form = NewCustomer(request.POST or None)
				context = {
					"form": form,
				}
				return render(request, "profile.html", context)

def connections(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('auth_login'))
	else:
		return render(request, "home.html", {})

def billing(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('auth_login'))
	else:
		return render(request, "billing.html", {})

def billing_plans(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('auth_login'))
	else:
		return render(request, "billing.html", {})