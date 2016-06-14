from django.shortcuts import render
# from .models import subchart, custdb
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import *
from django.db import models
from .models import cust_db_model


# Create your views here.
# REPLACE all these with variables- that come from the URL (IE by who is logged in, and what is begin searched)
# user = request.get(id=user_id)

def datapull(request, datasource, dataID):
   	if request.user.is_authenticated():
   		current_user=cust_db_model.objects.get(user_current=request.user).user_current
   		DBS_NAME = str(cust_db_model.objects.get(user_current=request.user).db_name)
		COLLECTION_NAME = str(cust_db_model.objects.get(user_current=request.user).db_collection)
		SEARCH_KEY= str(cust_db_model.objects.get(user_current=request.user).search_id)
		SEARCH_VALUE = int(dataID)
   		MONGODB_HOST = 'localhost'
		MONGODB_PORT = 27017
		# FIELDS = {'cust_id': True, 'cust_email': True, 'touchpoint_type': True, 'touchpoint_datasource': True, 'touchpoint_background': True, 'touchpoint_date': True, 'touchpoint_month': True,'touchpoint_name': True,'touchpoint_category': True,'touchpoint_owner': True,'touchpoint_amount': True,'touchpoint_count': True,'_id': False}
		

	   	connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
	   	collection = connection[DBS_NAME][COLLECTION_NAME]
	    # entries = collection.find(projection=FIELDS, limit=100000)
	   	entries = collection.find({SEARCH_KEY: SEARCH_VALUE})
	   	connection.close()
	   	return HttpResponse(dumps(entries), content_type="application/json")
	else:
		return HttpResponse('Please Log In')