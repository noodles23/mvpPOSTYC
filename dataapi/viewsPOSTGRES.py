from django.shortcuts import render
# from .models import subchart, custdb
import psycopg2
import json
from bson import json_util
from bson.json_util import dumps
from django.http import JsonResponse, HttpResponse

# Create your views here.
# REPLACE all these with variables- that come from the URL (IE by who is logged in, and what is begin searched)
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = '29ctest'
COLLECTION_NAME = 'custtest123'
FIELDS = {'cust_id': True, 'cust_email': True, 'touchpoint_type': True, 'touchpoint_datasource': True, 'touchpoint_background': True, 'touchpoint_date': True, 'touchpoint_month': True,'touchpoint_name': True,'touchpoint_category': True,'touchpoint_owner': True,'touchpoint_amount': True,'touchpoint_count': True,'_id': False}
# usertt = request.user
# user = User.objects.get(id=user_id)

db_name = 'wtf123'
db_user = 'postgres'
db_host = 'localhost'
db_password = 'Caroline1'



def datapull(request):
    conn = psycopg2.connect(dbname="wtf123", user="postgres", host="localhost", password="Caroline1")
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    rows = cur.fetchall()

    return HttpResponse(dumps(rows), content_type="application/json")

    # collection = connection[DBS_NAME][COLLECTION_NAME]
    # entries = collection.find(projection=FIELDS, limit=100000)
    # entries = collection.find()
    # connection.close()
   