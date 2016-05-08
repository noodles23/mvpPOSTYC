from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from .models import Conn
from pmain.models import CustomerDB

class connForm(ModelForm):
    class Meta:
        model = Conn
        fields = ['name', 'connection_type', 'username_or_apikey', 'password_if_required']

@login_required
def conn_list(request, template_name='conn/conn_list.html'):
    if request.user.is_superuser:
        conn = Conn.objects.all()
    else:
        conn = Conn.objects.filter(user=request.user)
    try:
        t = CustomerDB.objects.filter(customer_username=request.user).latest('updated')
        stat=t.customer_status
        if stat == None:
                stat = 'new'
        data = {
                "stat": stat,
                "object_list": conn
                }
    except:
        stat='new'
        data = {
                "stat": stat,
                "object_list": conn
                }
    # data = {}
    # data['object_list'] = conn
    return render(request, template_name, data)

@login_required
def conn_create(request, template_name='conn/conn_form.html'):
    form = connForm(request.POST or None)
    if form.is_valid():
        conn = form.save(commit=False)
        conn.user = request.user
        conn.save()
        return redirect('conn_list')
    return render(request, template_name, {'form':form})

@login_required
def conn_update(request, pk, template_name='conn/conn_form.html'):
    if request.user.is_superuser:
        conn= get_object_or_404(Conn, pk=pk)
    else:
        conn= get_object_or_404(Conn, pk=pk, user=request.user)
    form = connForm(request.POST or None, instance=conn)
    if form.is_valid():
        form.save()
        return redirect('conn_list')
    return render(request, template_name, {'form':form})

@login_required
def conn_delete(request, pk, template_name='conn/conn_confirm_delete.html'):
    if request.user.is_superuser:
        conn= get_object_or_404(Conn, pk=pk)
    else:
        conn= get_object_or_404(Conn, pk=pk, user=request.user)
    if request.method=='POST':
        conn.delete()
        return redirect('conn_list')
    return render(request, template_name, {'object':conn})