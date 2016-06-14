from django.shortcuts import render
from woocommerce import API
import psycopg2
import psycopg2.extras
import json
from bson import json_util
from bson.json_util import dumps
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import *
from django.db import models
from peewee import *


def dapi(request):
	wcapi = API(url="https://wptt123-noodles23.rhcloud.com/", consumer_key="ck_7910a71676e76033f7f483aaac148f5215a2e689", consumer_secret="cs_c113f96daede7643cb18cca090e73239eb68cd9e")
	my_query = wcapi.get("orders")
	return HttpResponse(my_query, content_type="application/json")

def dwrite(request):
	db_name='wtf123'
	db_user = 'postgres'
	db_host = 'localhost'
	db_password = 'Caroline'
	conn = psycopg2.connect(dbname=db_name, user=db_user, host=db_host, password=db_password)
	cur = conn.cursor()
	my_query = cur.execute("""INSERT INTO ppl123 (personid, lastname, firstname, address, city) VALUES (1234564, 'AUTOTEST', 'Auto2', 'Auto Address', 'shiity city');""")
	conn.commit()
	conn.close()

	return HttpResponse('ok')
