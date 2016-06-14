from django.shortcuts import render, get_object_or_404, redirect

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import NewCustomer, NewAlert
from .models import CustomerDB, alertbox, subchart

from django.core.mail import send_mail

# Create your views here.

# def home2(request):
# 	if not request.user.is_authenticated():
# 		return HttpResponseRedirect(reverse('auth_login'))
# 	else:
# 		return render(request, "home.html", {})

def ese(request):
	alist = alertbox.objects.filter(alert_user=request.user)
	context = {
					"alist": alist,
				}
	return render(request, "play.html", context)

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
				alist = alertbox.objects.filter(alert_user=request.user).order_by('-alert_date')
				context = {
					"alist": alist,
				}
				return render(request, "home.html", context)
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
		send_mail('New Sub Data Ready', request.user, 'kirk@29thcentury.com', ['alex@29thcentury.com', 'monkey@29thcentury.com'], fail_silently=False)
		return HttpResponseRedirect(reverse('home'))

@login_required
def alertform(request):
	form = NewAlert(request.POST or None)
	if request.method == 'POST' and form.is_valid():
			stock = form.save(commit=False)
			stock.save()
			return HttpResponseRedirect(reverse('alertform'))
	else:
				context = {
					"form": form,
				}
				return render(request, "alertform.html", context)
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

def result(request, searchvar):
	# user = User.objects.get(id=user_id)
	try:
		searchresult=subchart.objects.get(chart_name=searchvar)
		searchdescription=subchart.objects.get(chart_name=searchvar).chart_exp
		searchbase=subchart.objects.get(chart_name=searchvar).chart_base
		chartgroup=subchart.objects.get(chart_name=searchvar).chart_parent_id
		chartgroupTitle=subchart.objects.get(chart_name=searchvar).chart_title
		queryset = subchart.objects.filter(chart_parent_id=chartgroup).exclude(chart_name=searchvar)
		context = {
			"searchresult": searchresult,
			"searchdescription": searchdescription,
			"searchbase": searchbase,
			"chartgroup": chartgroup,
			"chartgroupTitle": chartgroupTitle,
			"queryset": queryset
		}
		return render(request, "dash_home.html", context)
	except:
		return render(request, "dash_home.html", {})

def cust(request, searchname):
	try:
		cust_name=custdb.objects.get(cust_email=searchname).cust_name
		cust_email=custdb.objects.get(cust_email=searchname).cust_email
		cust_gender=custdb.objects.get(cust_email=searchname).cust_gender
		cust_agegroup=custdb.objects.get(cust_email=searchname).cust_agegroup
		cust_address=custdb.objects.get(cust_email=searchname).cust_address
		cust_state=custdb.objects.get(cust_email=searchname).cust_state
		cust_country=custdb.objects.get(cust_email=searchname).cust_country
		cust_status=custdb.objects.get(cust_email=searchname).cust_status
		cust_table=custdb.objects.get(cust_email=searchname).cust_table
		cust_special=custdb.objects.get(cust_email=searchname).cust_special
		cust_joindate=custdb.objects.get(cust_email=searchname).cust_joindate
		cust_lastactive=custdb.objects.get(cust_email=searchname).cust_lastactive
		cust_referredby=custdb.objects.get(cust_email=searchname).cust_referredby
		cust_id=custdb.objects.get(cust_email=searchname).cust_id
		searchbase=custdb.objects.get(cust_email=searchname).cust_table
		context = {
			"cust_name": cust_name,
			"cust_id": cust_id,
			"cust_email": cust_email,
			"cust_gender": cust_gender,
			"cust_agegroup": cust_agegroup,
			"cust_address": cust_address,
			"cust_state": cust_state,
			"cust_country": cust_country,
			"cust_status": cust_status,
			"cust_special": cust_special,
			"cust_joindate": cust_joindate,
			"cust_referredby": cust_referredby,
			"cust_lastactive": cust_lastactive,
			"cust_table": cust_table,
			"searchbase": searchbase
		}
		foo=request.session.get('searchname')
		return render(request, "dash_cust.html", context)
	except:
		return render(request, "dash_home.html", {})