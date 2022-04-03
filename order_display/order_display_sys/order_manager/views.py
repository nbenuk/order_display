from ast import Or
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from order_display_sys.order_manager.models import Order

from django.http import HttpResponse
from django.http import JsonResponse
import json 

def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')
from rest_framework.decorators import api_view

@api_view(["POST"])
@csrf_exempt
def new_order(request):
    response = ''
    if request.method == 'POST':
        order_ref = request.data.get('order_ref')
        order = Order(order_ref=order_ref, status = 'Pending')
        try:
            order.save()
            response = json.dumps([{'Success': 'Order Added'}])
        except:
            response = json.dumps([{'Error': 'Exception raised saving order to database'}])
            
    return HttpResponse(response, content_type='text/json')
def view_orders(request):
    if request.method == 'GET':
        try:
            response = []
            orders = Order.objects.all()
            for order in orders:
                response.append( {"order_ref": order.order_ref, "status": order.status})
        except:
            response = json.dumps([{ 'Error' : 'Exception raised querying database'}])
    return JsonResponse(response, safe=False)

@api_view(["PUT"])
@csrf_exempt
def update_status(request):
    if request.method == 'PUT':
        order_ref = request.data.get('order_ref')
        status = request.data.get('status')
        order = Order.objects.get(order_ref=order_ref)

        order.status = status
        order.save()
        try:
            response = []
            orders = Order.objects.get(order_ref=order_ref)
        except:
            response = json.dumps([{ 'Error' : 'Exception raised querying database'}])
    return JsonResponse(response, safe=False)

@api_view(["DELETE"])
@csrf_exempt
def delete_order(request):
    if request.method == 'DELETE':
        order_ref = request.data.get('order_ref')
        Order.objects.filter(order_ref=order_ref).delete()
        try:
            response = []
        except:
            response = json.dumps([{ 'Error' : 'Exception raised querying database'}])
    return JsonResponse(response, safe=False)

