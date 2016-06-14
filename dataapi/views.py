from django.shortcuts import render
# from .models import subchart, custdb
import psycopg2
import psycopg2.extras
import json
from bson import json_util
from bson.json_util import dumps
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import *
from django.db import models
from .models import cust_db_model
# Create your views here.
# REPLACE all these with variables- that come from the URL (IE by who is logged in, and what is begin searched)

# db_name = str('wtf123')
# db_user = str('postgres')
# db_host = str('localhost')
# db_password = str('Caroline1')


def datapull(request, datasource, dataID):
	if request.user.is_authenticated():
	    current_user=cust_db_model.objects.get(user_current=request.user).user_current
	    SEARCH_VALUE = int(dataID)
	    my_query = query_db("SELECT * FROM %s WHERE cust_id='%s';" %(datasource, dataID), current_user, (3,))
	    return HttpResponse(dumps(my_query), content_type="application/json")
	else:
		return HttpResponse('Please Log In')

def db(database_name='wtf123'):
    return psycopg2.connect(database=database_name)

def query_db(query, useridt, args=(), one=False):
    db_name=str(cust_db_model.objects.get(user_current=useridt).db_name)
    db_user = str(cust_db_model.objects.get(user_current=useridt).db_username)
    db_host = str(cust_db_model.objects.get(user_current=useridt).db_host)
    db_password = str(cust_db_model.objects.get(user_current=useridt).db_password)
    conn = psycopg2.connect(dbname=db_name, user=db_user, host=db_host, password=db_password)
    cur = conn.cursor()
    cur.execute(query, args)
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    return (r[0] if r else None) if one else r
