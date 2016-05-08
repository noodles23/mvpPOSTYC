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

# def home2(request):
# 	if not request.user.is_authenticated():
# 		return HttpResponseRedirect(reverse('auth_login'))
# 	else:
# 		return render(request, "home.html", {})

def home(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('auth_login'))
	else:
		try:
			t = CustomerDB.objects.filter(customer_username=request.user).latest('updated')
			if t.customer_status=='awaiting':
				stat="awaiting"
				context = {
					"stat": stat,
					}
			elif t.customer_status=='ready':
				stat="ready"
				return render(request, "home.html", {})
			else:
				stat="new"
				context = {
					"stat": stat,
					}
			return render(request, "home_init.html", context)
		except:
			stat="new"
			context = {
					"stat": stat,
					}
			return render(request, "home_init.html", context)

def tt(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('auth_login'))
	else:
		t = CustomerDB.objects.filter(customer_username=request.user).latest('updated')
		t.customer_status = 'awaiting'  # change field
		t.save() # this will update only
		return HttpResponseRedirect(reverse('home'))

@login_required
def profile(request):
	form = NewCustomer(request.POST or None)
	try:
		t = CustomerDB.objects.filter(customer_username=request.user).latest('updated')
		stat=t.customer_status
		if request.method == 'POST' and form.is_valid() and (stat == "awaiting" or stat == "ready"):
			stock = form.save(commit=False)
			stock.customer_username = request.user
			stock.customer_email = request.user.email
			stock.form_status = 'completed'
			stock.customer_status = stat
			stock.save()
			return HttpResponseRedirect(reverse('conn_list'))
		elif request.method == 'POST' and form.is_valid():
			stock = form.save(commit=False)
			stock.customer_username = request.user
			stock.customer_email = request.user.email
			stock.form_status = 'completed'
			stock.customer_status = 'new'
			stock.save()
			return HttpResponseRedirect(reverse('conn_list'))
		else:
			try: 
				search_id = request.user
				initialsetup = False
				queryset = CustomerDB.objects.filter(customer_username=search_id).latest('updated')
				form = NewCustomer(
					request.POST or None,
					initial={'customer_name': queryset.customer_name, 'company_website': queryset.company_website, 'company_name': queryset.company_name, 'company_country': queryset.company_country, 'company_primary_currency': queryset.company_primary_currency, }
					)
				context = {
					"form": form,
					"queryset": queryset,
					"initialsetup": initialsetup
				}
				return render(request, "profile.html", context)
			except:
				form = NewCustomer(request.POST or None)
				initialsetup = True
				context = {
					"form": form,
					"initialsetup": initialsetup
				}
				return render(request, "profile.html", context)
	except:
		if request.method == 'POST' and form.is_valid():
			stock = form.save(commit=False)
			stock.customer_username = request.user
			stock.customer_email = request.user.email
			stock.form_status = 'completed'
			stock.customer_status = 'new'
			stock.save()
			return HttpResponseRedirect(reverse('conn_list'))
		elif request.method == 'POST' and form.is_valid():
			stock = form.save(commit=False)
			stock.customer_username = request.user
			stock.customer_email = request.user.email
			stock.form_status = 'completed'
			stock.customer_status = 'new'
			stock.save()
			return HttpResponseRedirect(reverse('conn_list'))
		else:
			try: 
				search_id = request.user
				initialsetup = False
				queryset = CustomerDB.objects.filter(customer_username=search_id).latest('updated')
				form = NewCustomer(
					request.POST or None,
					initial={'customer_name': queryset.customer_name, 'company_website': queryset.company_website, 'company_name': queryset.company_name, 'company_country': queryset.company_country, 'company_primary_currency': queryset.company_primary_currency, }
					)
				context = {
					"form": form,
					"queryset": queryset,
					"initialsetup": initialsetup
				}
				return render(request, "profile.html", context)
			except:
				form = NewCustomer(request.POST or None)
				initialsetup = True
				context = {
					"form": form,
					"initialsetup": initialsetup
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
		try:
			t = CustomerDB.objects.filter(customer_username=request.user).latest('updated')
			stat=t.customer_status
			if stat == None:
				stat = 'new'
			context = {
					"stat": stat,
					}
		except:
			stat='new'
			context = {
					"stat": stat,
					}
		return render(request, "billing.html", context)

def billing_plans(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('auth_login'))
	else:
		return render(request, "billing.html", {})