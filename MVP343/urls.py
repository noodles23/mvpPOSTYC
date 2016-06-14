"""MVP343 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from connectionCRUD import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'pmain.views.home', name='home'),
    url(r'^profile/$', 'pmain.views.profile', name='profile'),
    # url(r'^connections/$', 'pmain.views.connections', name='connections'),
    url(r'^billing/$', 'pmain.views.billing', name='billing'),
    url(r'^accounts/', include('registration.backends.default.urls')),

    #tt is the link that changes a user from New to Pending at the end of the initial setup process
    url(r'^tt/$', 'pmain.views.tt', name='tt'),
    url(r'^alertform/$', 'pmain.views.alertform', name='alertform'),

    # Random testing playround page
    # url(r'^ese/$', 'pmain.views.ese', name='ese'),

    # url(r'^c=(?P<searchname>\S+)/$', 'pmain.views.cust', name='cust'),
    # url(r'^v=(?P<searchvar>\S+)/$', 'pmain.views.result', name='result'),

    url(r'^data/(?P<datasource>\S+)/(?P<dataID>[0-9]+)', 'dataapi.views.datapull', name='datapull'),
    url(r'^dapi/$', 'apiconnect.views.dapi', name='dapi'),
    # url(r'^dwrite/$', 'apiconnect.views.dwrite', name='dwrite'),

    # The CRUD for data connections
    url(r'^connections/', views.conn_list, name='conn_list'),
    url(r'^new$', views.conn_create, name='conn_new'),
    url(r'^edit/(?P<pk>\d+)$', views.conn_update, name='conn_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.conn_delete, name='conn_delete')
]
